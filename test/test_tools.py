import os
from pathlib import Path
from typing import Any

workspace_path="/Users/ailabuser7-1/Documents/cursor-workspace/react-agent-exp"

def find_directory(keyword: str) -> dict[str, Any]:
    """基于关键词查找目录路径。

    在工作空间内搜索包含关键词的目录名称，返回匹配的目录路径列表。

    Args:
        keyword: 用于搜索目录的关键词

    Returns:
        包含匹配目录路径列表的字典
    """
    matching_dirs = []
    
    # 遍历工作空间目录，查找包含关键词的目录
    for root, dirs, files in os.walk(workspace_path):
        # 检查当前目录名是否包含关键词
        current_dir = Path(root)
        print(current_dir)
        if keyword.lower() in current_dir.name.lower():
            # 获取相对于工作空间的路径
            rel_path = current_dir.relative_to(workspace_path)
            matching_dirs.append(str(rel_path))
    return {"matching_directories": matching_dirs, "count": len(matching_dirs)}

if __name__ == "__main__":
    print(find_directory("金融实证方法"))