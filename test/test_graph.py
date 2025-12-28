import asyncio
from pathlib import Path
from dotenv import load_dotenv

# 在导入其他模块之前加载 .env 文件
# 从项目根目录查找 .env 文件
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

from react_agent import graph
from react_agent.context import Context
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.runnables import RunnableConfig


async def test_react_agent_simple_passthrough() -> None:
    context = Context(system_prompt="You are a helpful AI assistant.")
    
    print("=" * 60)
    print("开始执行 ReAct Agent")
    print("=" * 60)
    
    step_count = 0
    final_result = None
    
    # 使用 astream 来获取每一步的输出
    async for chunk in graph.astream(
        {"messages": [("user", "抽取金融实证方法目录下考试要点和要点重要性（1-5）个等级，一共不要超过30条考试要点。")]},  # type: ignore,
        context=context,
        config=RunnableConfig(recursion_limit=50)
    ):
        step_count += 1
        print(f"\n[步骤 {step_count}]")
        print("-" * 60)
        
        # 遍历每个节点的输出
        for node_name, node_output in chunk.items():
            print(f"节点: {node_name}")
            print(f"节点输出: {node_output}")
            
            if node_name == "call_model":
                messages = node_output.get("messages", [])
                if messages:
                    last_msg = messages[-1]
                    if isinstance(last_msg, AIMessage):
                        print(f"模型响应: {last_msg.content}")
                        if last_msg.tool_calls:
                            print(f"工具调用:")
                            for tc in last_msg.tool_calls:
                                print(f"  - {tc.get('name', 'unknown')}: {tc.get('args', {})}")
            
            elif node_name == "tools":
                messages = node_output.get("messages", [])
                if messages:
                    print(f"工具执行结果 ({len(messages)} 条消息):")
                    for msg in messages:
                        if isinstance(msg, ToolMessage):
                            content_preview = str(msg.content)[:300]
                            print(f"  - {content_preview}...")
        
        # 保存最后一步的结果
        final_result = chunk
    
    print("\n" + "=" * 60)
    print("执行完成")
    print("=" * 60)
    
    # 获取完整的状态以进行断言（astream 只返回增量更新，需要获取完整状态）
    final_result = await graph.ainvoke(
        {"messages": [("user", "Who is the founder of LangChain?")]},  # type: ignore
        context=context,
    )
    
    print(f"\n最终消息数量: {len(final_result.get('messages', []))}")
    if final_result.get("messages"):
        final_content = str(final_result["messages"][-1].content)
        print(f"最终回答: {final_content[:500]}...")
    
    assert "harrison" in str(final_result["messages"][-1].content).lower()


if __name__ == "__main__":
    asyncio.run(test_react_agent_simple_passthrough())