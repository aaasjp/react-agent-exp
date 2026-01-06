# DeepAgents Documentation

## Overview

DeepAgents is an open-source agent architecture for building AI systems that can handle complex, multi-step tasks. Built on LangGraph and inspired by applications like Claude Code, Deep Research, and Manus, DeepAgents come with planning capabilities, file system tools for context management, and the ability to spawn subagents. This makes them well-equipped to handle complex agentic tasks that require planning, delegation, and persistent memory.

## Key Features

### 1. Planning and Task Decomposition

DeepAgents include a built-in `write_todos` tool that enables agents to break down complex tasks into discrete steps, track progress, and adapt plans as new information emerges. This allows agents to handle long-horizon tasks effectively, with the ability to plan before execution and update plans dynamically during execution.

### 2. Context Management

File system tools (`ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep`) allow agents to offload large context to memory, preventing context window overflow and enabling work with variable-length tool results. This is critical for tasks that involve extensive data or require the agent to work with large files.

### 3. Subagent Spawning

A built-in `task` tool enables agents to spawn specialized subagents for context isolation. This keeps the main agent’s context clean while still going deep on specific subtasks. Subagents can be used for parallel execution of multiple subtasks, and the main agent can reconcile these results into a coherent final output.

### 4. Long-Term Memory

DeepAgents can maintain persistent memory across threads using LangGraph’s Store. This allows agents to save and retrieve information from previous conversations, enabling them to handle tasks that span multiple sessions or require long-term tracking of progress, with support for hybrid memory systems that combine ephemeral and persistent storage.

### 5. Middleware Integration

DeepAgents use middleware under the hood to provide the following capabilities:

| Middleware | Purpose |
| --- | --- |
| **TodoListMiddleware** | Task planning and progress tracking |
| **FilesystemMiddleware** | File operations and context offloading (auto-saves large results) |
| **SubAgentMiddleware** | Delegate tasks to isolated sub-agents |
| **SummarizationMiddleware** | Auto-summarizes when context exceeds 170k tokens |
| **AnthropicPromptCachingMiddleware** | Caches system prompts to reduce costs (Anthropic only) |
| **PatchToolCallsMiddleware** | Fixes dangling tool calls from interruptions |
| **HumanInTheLoopMiddleware** | Pauses execution for human approval (requires `interrupt_on` config)

## Use Cases

DeepAgents are particularly well-suited for:

### 1. Deep Research and Market Analysis

Deep agents can perform comprehensive research by breaking down research questions into sub-tasks, spawning sub-agents to collect data on competitors, pricing, and positioning, extracting data from reports, websites, and PDFs, comparing findings and flagging inconsistencies, and producing structured outputs such as memos or tables with citations and references.

### 2. Software Engineering and Coding Projects

Deep agents can manage the entire development workflow, including reading and understanding repositories, performing task decomposition for features or refactoring, implementing changes across multiple files, running tests and fixing failures, and writing documentation and changelogs with proper code formatting and style guides.

### 3. Large-Scale Refactoring and Migration

Deep agents are especially useful for complex migrations such as framework upgrades, API changes, or moving from monolith to services. In these use cases, a deep agent can inventory the existing system, identify dependencies and risk areas, plan migration steps, execute changes incrementally, and validate parity after each stage.

### 4. Incident Analysis and Postmortems

Deep agents can perform incident response analysis by pulling logs, metrics, and alerts, reconstructing timelines, forming and testing hypotheses, identifying root causes, and generating postmortem documents.

### 5. Compliance, Audit, and Documentation Preparation

Deep agents can handle compliance work by parsing regulatory requirements, mapping controls to internal documents, identifying gaps, requesting missing evidence, and assembling audit-ready folders.

### 6. RFP, Proposal, and Sales Engineering Workflows

Deep agents can handle RFPs and prepare proposals by parsing requirements, retrieving relevant case studies, drafting responses aligned with constraints, ensuring consistent messaging, and producing final proposal documents.

### 7. Knowledge Base Maintenance and Internal Enablement

Deep agents can maintain knowledge bases by detecting recurring questions or issues, proposing updates to documentation, rewriting outdated pages, and maintaining cross-links between topics.

### 8. Financial Analysis and Reconciliation

Deep agents can help with financial workflows by performing invoice reconciliation, spend categorization, contract vs usage comparisons, and cost optimization analysis.

## Framework Integration

DeepAgents are built on top of:

* [LangGraph](/oss/python/langgraph/overview) - Provides the underlying graph execution and state management
* [LangChain](/oss/python/langchain/overview) - Tools and model integrations work seamlessly with deep agents
* [LangSmith](/langsmith/home) - For observability, evaluation, and deployment

DeepAgents applications can be deployed via [LangSmith Deployment](/langsmith/deployments) and monitored with [LangSmith Observability](/langsmith/observability).

## Getting Started

### Step 1: Installation

```
pip install deepagents tavily-python
```

### Step 2: Set up your API keys

```
export ANTHROPIC_API_KEY="your-api-key" export TAVILY_API_KEY="your-tavily-api-key"
```

### Step 3: Create a search tool

```
import os from typing import Literal from tavily import TavilyClient def internet_search(query: str, max_results: int = 5, topic: Literal["general", "news", "finance"] = "general", include_raw_content: bool = False):
    """Run a web search"""
    return tavily_client.search(query, max_results=max_results, include_raw_content=include_raw_content, topic=topic)
```

### Step 4: Create a deep agent

```
research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report. You have access to an internet search tool as your primary means of gathering information. You can specify the max number of results to return, the topic, and whether raw content should be included.
```

```
agent = create_deep_agent(tools=[internet_search], system_prompt=research_instructions)
```

### Step 5: Run the agent

```
result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})

# Print the agent's response
print(result["messages"][-1].content)
```

## Built-In Tools

Every deep agent created with `create_deep_agent` comes with a standard set of tools:

| Tool Name | Description | Provided By |
| --- | --- | --- |
| `write_todos` | Create and manage structured task lists for tracking progress through complex workflows | TodoListMiddleware |
| `read_todos` | Read the current todo list state | TodoListMiddleware |
| `ls` | List all files in a directory (requires absolute path) | FilesystemMiddleware |
| `read_file` | Read content from a file with optional pagination (offset/limit parameters) | FilesystemMiddleware |
| `write_file` | Create a new file or completely overwrite an existing file | FilesystemMiddleware |
| `edit_file` | Perform exact string replacements in files | FilesystemMiddleware |
| `glob` | Find files matching a pattern (e.g., `**/*.py`) | FilesystemMiddleware |
| `grep` | Search for text patterns within files | FilesystemMiddleware |
| `execute` | Run shell commands in a sandboxed environment (only if backend implements SandboxBackendProtocol) | FilesystemMiddleware |
| `task` | Delegate tasks to specialized sub-agents with isolated context windows | SubAgentMiddleware |

## Security Considerations

### Trust Model

DeepAgents follow a "trust the LLM" model similar to Claude Code. The agent can perform any action the underlying tools allow. Security boundaries should be enforced at the tool/sandbox level, not by expecting the LLM to self-police.

## Deployment

Deploying deep agentic systems needs careful planning. Unlike stateless APIs, deep agents keep state, memory, and artifacts, which affects infrastructure, monitoring, and costs.

Production deployment often includes logging, evaluation hooks, and safeguards to prevent runaway behavior. Platforms built by organizations like Anthropic and OpenAI emphasize controlled tool access and safety boundaries.

A successful deployment treats agentic systems as long-running processes rather than ephemeral requests, aligning infrastructure with their long-horizon nature.

## Key Takeaways

Deep agents represent a shift from reactive AI to structured, goal-driven systems. They shine when automation must handle complex, real-world work that spans multiple steps and requires persistent memory. Used correctly, they make agents not just powerful, but practical and production-ready.

* Agentic systems are designed for long-horizon, multi-step tasks, not single-step interactions
* Task decomposition and sub-agents enable systems to tackle complex projects reliably
* Context management and external memory are essential for stable behavior
* Frameworks like LangChain and LangGraph provide structure for agentic workflows
* Coding, deep research, and market analysis are proven deep agent use cases
* Prompts define behavior, but architecture defines reliability
* Human-in-the-loop controls are critical for production-ready systems