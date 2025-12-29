"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

import json
import os
import sys
from pathlib import Path
from typing import Any, Callable, List, Optional, cast

from langchain_tavily import TavilySearch
from langgraph.runtime import get_runtime

from react_agent.context import Context


workspace_path="/Users/ailabuser7-1/Documents/cursor-workspace/react-agent-exp/data"
workspace_path="C:\\Users\\aaasj\\Documents\\cursor_workspace\\react-agent-exp\\data"

async def search(query: str) -> Optional[dict[str, Any]]:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    runtime = get_runtime(Context)
    wrapped = TavilySearch(max_results=runtime.context.max_search_results)
    return cast(dict[str, Any], await wrapped.ainvoke({"query": query}))


async def find_directory(keyword: str) -> dict[str, Any]:
    """基于关键词查找目录路径。

    在工作空间内搜索包含关键词的目录名称，返回匹配的目录路径列表。

    Args:
        keyword: 用于搜索目录的关键词

    Returns:
        包含以下字段的字典:
        - matching_directories: 匹配的目录路径列表
        - count: 匹配目录的数量
        - keyword: 搜索使用的关键词
        - workspace_path: 工作空间的根路径
    """
    matching_dirs = []
    # 遍历工作空间目录，查找包含关键词的目录
    print(f"--------------------------------workspace_path: {workspace_path}")
    for root, dirs, files in os.walk(workspace_path):
        # 检查当前目录名是否包含关键词
        current_dir = Path(root)
        print(f"--------------------------------current_dir: {current_dir}")
        if keyword.lower() in current_dir.name.lower():
            # 获取相对于工作空间的路径
            rel_path = current_dir.relative_to(workspace_path)
            matching_dirs.append(str(rel_path))
    
    result = {
        "matching_directories": matching_dirs,
        "count": len(matching_dirs),
        "keyword": keyword,
        "workspace_path": workspace_path
    }
    return result
    return {
        "matching_directories": matching_dirs, 
        "count": len(matching_dirs), 
        "keyword": keyword, 
        "workspace_path": workspace_path,
    }


def _has_markdown_files(directory: Path) -> bool:
    """检查目录中是否包含 markdown 文件。
    
    Args:
        directory: 要检查的目录路径
        
    Returns:
        如果目录中包含 .md 文件则返回 True，否则返回 False
    """
    try:
        for item in directory.iterdir():
            if item.is_file() and item.suffix.lower() == '.md':
                return True
            elif item.is_dir():
                # 递归检查子目录
                if _has_markdown_files(item):
                    return True
    except (PermissionError, OSError):
        return False
    return False


async def list_directory_files(path: str) -> dict[str, Any]:
    """递归列出给定目录下所有 markdown 格式的文件。

    递归遍历目录及其所有子目录，返回所有 .md 文件的相对路径列表。

    Args:
        path: 目录路径（相对于工作空间根目录或绝对路径）

    Returns:
        包含文件路径列表的字典，格式如 ["a/b/c.md", "a/e/f/d.md"]
    """
    
    # 处理相对路径和绝对路径
    workspace_path_obj = Path(workspace_path)
    if os.path.isabs(path):
        target_path = Path(path)
    else:
        target_path = workspace_path_obj / path
    
    if not target_path.exists():
        return {"error": f"路径不存在: {path}", "files": []}
    
    if not target_path.is_dir():
        return {"error": f"路径不是目录: {path}", "files": []}
    
    files = []
    
    try:
        # 递归遍历目录，查找所有 .md 文件
        for item in target_path.rglob("*.md"):
            if item.is_file():
                rel_path = item.relative_to(workspace_path_obj)
                files.append(str(rel_path))
        
        # 按路径排序
        files.sort()
        
        result = {
            "path": str(target_path.relative_to(workspace_path_obj)),
            "files": files,
            "file_count": len(files)
        }
        return result
    except PermissionError:
        return {"error": f"没有权限访问目录: {path}", "files": []}
    except Exception as e:
        return {"error": f"遍历目录时出错: {str(e)}", "files": []}


async def read_file(path: str) -> dict[str, Any]:
    """读取文件内容。

    读取指定路径的文件内容。

    Args:
        path: 文件路径（相对于工作空间根目录或绝对路径）

    Returns:
        包含文件内容的字典
    """    
    # 处理相对路径和绝对路径
    workspace_path_obj = Path(workspace_path)
    if os.path.isabs(path):
        target_path = Path(path)
    else:
        target_path = workspace_path_obj / path
    
    if not target_path.exists():
        return {"error": f"文件不存在: {path}", "content": None}
    
    if not target_path.is_file():
        return {"error": f"路径不是文件: {path}", "content": None}
    
    try:
        # 尝试以UTF-8编码读取，如果失败则尝试其他编码
        try:
            content = target_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            # 如果UTF-8失败，尝试使用latin-1或二进制模式
            try:
                content = target_path.read_text(encoding="latin-1")
            except Exception:
                return {
                    "error": f"无法读取文件（可能是二进制文件）: {path}",
                    "content": None,
                    "path": str(target_path.relative_to(workspace_path_obj))
                }
        content=content[:1000]
        result = {
            "path": str(target_path.relative_to(workspace_path_obj)),
            "content": content,
            "size": target_path.stat().st_size,
            "lines": len(content.splitlines())
        }
        return result
    except PermissionError:
        return {"error": f"没有权限读取文件: {path}", "content": None}
    except Exception as e:
        return {"error": f"读取文件时出错: {str(e)}", "content": None}


TOOLS: List[Callable[..., Any]] = [search, find_directory, list_directory_files, read_file]
