"""Define a custom Reasoning and Action agent.

Works with a chat model with tool calling support.
"""

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Dict, List, Literal, cast

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from langgraph.runtime import Runtime

from react_agent.context import Context
from react_agent.state import InputState, State
from react_agent.tools import TOOLS
from react_agent.utils import load_chat_model


async def workspace_index(
    state: State, runtime: Runtime[Context]
) -> Dict[str, List[AIMessage]]:
    """对 workspace 目录进行索引和分析。
    
    该函数会：
    1. 扫描 workspace 目录结构
    2. 收集文档内容（特别是 markdown 文件）
    3. 使用大模型分析目录结构和内容
    4. 返回结构化的 JSON 分析结果
    
    Args:
        state: 当前状态
        runtime: 运行时上下文，包含 workspace_path 等配置
        
    Returns:
        包含结构化 JSON 分析结果的 AIMessage 列表
    """
    workspace_path = runtime.context.workspace_path
    workspace_path_obj = Path(workspace_path)
    
    # 1. 扫描目录结构
    directory_structure = {}
    markdown_files = []
    directory_paths = []  # 收集所有目录路径
    
    if not workspace_path_obj.exists():
        error_result = {
            "error": f"工作空间路径不存在: {workspace_path}",
            "workspace_path": workspace_path,
            "directory_structure_paths": [],
            "document_count": 0,
            "directory_count": 0,
            "analysis_report": ""
        }
        error_msg = AIMessage(content=json.dumps(error_result, ensure_ascii=False, indent=2))
        return {"messages": [error_msg]}
    
    # 递归遍历目录，构建目录树结构并统计信息
    def build_directory_tree(path: Path, max_depth: int = 5, current_depth: int = 0) -> dict:
        """构建目录树结构"""
        if current_depth >= max_depth:
            return {"type": "directory", "truncated": True}
        
        # 记录目录路径（排除根目录本身）
        if current_depth > 0:
            rel_path = str(path.relative_to(workspace_path_obj))
            if rel_path not in directory_paths:
                directory_paths.append(rel_path)
        
        tree = {
            "type": "directory",
            "name": path.name,
            "path": str(path.relative_to(workspace_path_obj)),
            "children": []
        }
        
        try:
            items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
            for item in items:
                if item.is_dir():
                    # 跳过隐藏目录和常见的不需要索引的目录
                    if not item.name.startswith('.') and item.name not in ['__pycache__', 'node_modules']:
                        tree["children"].append(build_directory_tree(item, max_depth, current_depth + 1))
                elif item.is_file():
                    # 收集 markdown 文件
                    if item.suffix.lower() == '.md':
                        markdown_files.append(str(item.relative_to(workspace_path_obj)))
                        tree["children"].append({
                            "type": "file",
                            "name": item.name,
                            "path": str(item.relative_to(workspace_path_obj)),
                            "size": item.stat().st_size
                        })
        except (PermissionError, OSError) as e:
            tree["error"] = str(e)
        
        return tree
    
    directory_structure = build_directory_tree(workspace_path_obj)
    
    # 统计目录个数（递归统计目录树中的所有目录）
    def count_directories(tree: dict) -> int:
        """递归统计目录树中的目录数量"""
        count = 0
        if tree.get("type") == "directory" and not tree.get("truncated"):
            count = 1
            for child in tree.get("children", []):
                count += count_directories(child)
        return count
    
    directory_count = count_directories(directory_structure)
    document_count = len(markdown_files)
    
    # 2. 收集文档内容（读取前 N 个 markdown 文件的内容摘要）
    document_contents = []
    max_files_to_read = 20  # 限制读取的文件数量，避免内容过长
    preview_length = 2000  # 每个文件预览的最大字符数
    
    for file_path in markdown_files[:max_files_to_read]:
        try:
            full_path = workspace_path_obj / file_path
            # 高效读取文件前 N 个字符作为摘要
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(preview_length)
            document_contents.append({
                "path": file_path,
                "content_preview": content,
                "size": full_path.stat().st_size
            })
        except Exception as e:
            document_contents.append({
                "path": file_path,
                "error": f"读取文件失败: {str(e)}"
            })
    
    # 3. 构建分析提示
    analysis_prompt = f"""请对以下工作空间目录结构和文档内容进行深入分析。

工作空间路径: {workspace_path}

## 目录结构
{json.dumps(directory_structure, ensure_ascii=False, indent=2)}

## 文档内容摘要（共 {len(markdown_files)} 个 markdown 文件，已读取前 {min(len(markdown_files), max_files_to_read)} 个）
{json.dumps(document_contents, ensure_ascii=False, indent=2)}

## 分析要求
请提供以下分析：

1. **目录结构分析**：
   - 整体目录组织方式
   - 主要目录分类和用途
   - 目录之间的层级关系

2. **文档内容分析**：
   - 文档主题和内容领域
   - 文档之间的关联性
   - 主要知识点和概念

3. **内容总结**：
   - 工作空间的主要内容领域
   - 知识体系结构
   - 关键信息点

请用中文详细回答，结构清晰，便于理解。"""

    # 4. 使用大模型进行分析
    try:
        model = load_chat_model(runtime.context.model)
        
        system_message = """你是一个专业的文档分析助手。你的任务是分析工作空间的目录结构和文档内容，
提供深入的结构化分析和建议。请确保分析全面、准确、有条理。"""
        
        # 统一使用消息对象格式，保持与 call_model 的一致性
        response = await model.ainvoke([
            SystemMessage(content=system_message),
            HumanMessage(content=analysis_prompt)
        ])
        
        # 提取模型的分析报告
        analysis_report = ""
        if hasattr(response, 'content'):
            if isinstance(response.content, str):
                analysis_report = response.content
            elif isinstance(response.content, list):
                # 处理内容为列表的情况
                analysis_report = " ".join(str(item) for item in response.content)
            else:
                analysis_report = str(response.content)
        else:
            analysis_report = "模型响应格式异常，无法提取分析报告"
    except Exception as e:
        # 如果模型调用失败，记录错误但继续返回目录结构信息
        analysis_report = f"模型分析失败: {str(e)}"
    
    # 5. 构建结构化的 JSON 返回结果
    result = {
        "workspace_path": workspace_path,
        "directory_structure_paths": sorted(directory_paths),  # 所有目录路径列表
        "document_count": document_count,  # 文档个数
        "directory_count": directory_count,  # 目录个数
        "analysis_report": analysis_report,  # 模型返回的分析总结报告
        "directory_structure": directory_structure,  # 完整的目录结构树
        "document_files": markdown_files  # 所有文档文件路径列表
    }
    
    # 将结果格式化为 JSON 字符串，通过 AIMessage 返回
    result_json = json.dumps(result, ensure_ascii=False, indent=2)
    result_msg = AIMessage(content=result_json)
    
    return {"messages": [result_msg]}

# Define the function that calls the model
async def call_model(
    state: State, runtime: Runtime[Context]
) -> Dict[str, List[AIMessage]]:
    """Call the LLM powering our "agent".

    This function prepares the prompt, initializes the model, and processes the response.

    Args:
        state (State): The current state of the conversation.
        config (RunnableConfig): Configuration for the model run.

    Returns:
        dict: A dictionary containing the model's response message.
    """
    # Initialize the model with tool binding. Change the model or add more tools here.
    model = load_chat_model(runtime.context.model).bind_tools(TOOLS)

    # Format the system prompt. Customize this to change the agent's behavior.
    system_message = runtime.context.system_prompt.format(
        system_time=datetime.now(tz=UTC).isoformat()
    )

    # Get the model's response
    response = cast( # type: ignore[redundant-cast]
        AIMessage,
        await model.ainvoke(
            [{"role": "system", "content": system_message}, *state.messages]
        ),
    )

    # Handle the case when it's the last step and the model still wants to use a tool
    if state.is_last_step and response.tool_calls:
        return {
            "messages": [
                AIMessage(
                    id=response.id,
                    content="Sorry, I could not find an answer to your question in the specified number of steps.",
                )
            ]
        }

    # Return the model's response as a list to be added to existing messages
    return {"messages": [response]}


# Define a new graph

builder = StateGraph(State, input_schema=InputState, context_schema=Context)

# Define the two nodes we will cycle between
builder.add_node(call_model)
builder.add_node("tools", ToolNode(TOOLS))
builder.add_node(workspace_index)

# Set the entrypoint as `call_model`
# This means that this node is the first one called
builder.add_edge("__start__", "workspace_index")
builder.add_edge("workspace_index", "call_model")


def route_model_output(state: State) -> Literal["__end__", "tools"]:
    """Determine the next node based on the model's output.

    This function checks if the model's last message contains tool calls.

    Args:
        state (State): The current state of the conversation.

    Returns:
        str: The name of the next node to call ("__end__" or "tools").
    """
    last_message = state.messages[-1]
    if not isinstance(last_message, AIMessage):
        raise ValueError(
            f"Expected AIMessage in output edges, but got {type(last_message).__name__}"
        )
    # If there is no tool call, then we finish
    if not last_message.tool_calls:
        return "__end__"
    # Otherwise we execute the requested actions
    return "tools"


# Add a conditional edge to determine the next step after `call_model`
builder.add_conditional_edges(
    "call_model",
    # After call_model finishes running, the next node(s) are scheduled
    # based on the output from route_model_output
    route_model_output,
)

# Add a normal edge from `tools` to `call_model`
# This creates a cycle: after using tools, we always return to the model
builder.add_edge("tools", "call_model")

# Compile the builder into an executable graph
# Note: recursion_limit should be set when invoking the graph, not during compilation
# Example: graph.invoke(inputs, {"recursion_limit": 100})
graph = builder.compile(name="ReAct Agent")
