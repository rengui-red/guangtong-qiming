"""
光通启明 · 数据加载工具
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional
from utils.logger import logger


def load_json(path: Path) -> Optional[Any]:
    """加载JSON文件"""
    try:
        if not path.exists():
            logger.warning(f"文件不存在：{path}")
            return None
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"JSON解析失败：{path} - {e}")
        return None
    except Exception as e:
        logger.error(f"加载失败：{path} - {e}")
        return None


def load_text(path: Path) -> Optional[str]:
    """加载文本文件"""
    try:
        if not path.exists():
            logger.warning(f"文件不存在：{path}")
            return None
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logger.error(f"加载失败：{path} - {e}")
        return None


def load_characters(path: Path) -> Dict[str, Dict]:
    """加载字源库，返回 {汉字: 数据} 格式"""
    data = load_json(path)
    if not data:
        return {}
    
    result = {}
    for item in data:
        char = item.get("汉字") or item.get("char")
        if char:
            result[char] = item
    logger.info(f"字源库加载完成：{len(result)} 字")
    return result


def load_cultural_graph(path: Path) -> Dict[str, Dict]:
    """加载文化关联图谱"""
    data = load_json(path)
    if not data:
        return {}
    
    graph = data.get("图谱", {})
    logger.info(f"文化图谱加载完成：{len(graph)} 字")
    return graph




