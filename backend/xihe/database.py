"""
光通启明 · 字源库加载
"""

from pathlib import Path
from typing import Dict, List, Optional
from utils.loader import load_characters, load_cultural_graph
from utils.logger import logger


class CharacterDatabase:
    """字源库"""
    
    def __init__(self, db_path: Path, graph_path: Path):
        self.db_path = db_path
        self.graph_path = graph_path
        self.characters: Dict[str, Dict] = {}
        self.cultural_graph: Dict[str, Dict] = {}
        self._load()
    
    def _load(self):
        self.characters = load_characters(self.db_path)
        self.cultural_graph = load_cultural_graph(self.graph_path)
    
    def get(self, char: str) -> Optional[Dict]:
        """获取单个汉字"""
        return self.characters.get(char)
    
    def search(self, keyword: str, limit: int = 10) -> List[Dict]:
        """按拼音或字义搜索"""
        keyword = keyword.lower()
        results = []
        for char, data in self.characters.items():
            pinyin = str(data.get("拼音", "")).lower()
            meaning = str(data.get("本义", "")) + str(data.get("现代常用义", ""))
            if keyword in pinyin or keyword in meaning or keyword in char:
                results.append(data)
                if len(results) >= limit:
                    break
        return results
    
    def get_cultural(self, char: str) -> Optional[Dict]:
        """获取文化关联"""
        return self.cultural_graph.get(char)
    
    def connect(self, char1: str, char2: str) -> Dict:
        """文明连接：找两个字之间的关联"""
        g1 = self.cultural_graph.get(char1, {})
        g2 = self.cultural_graph.get(char2, {})
        
        if not g1 or not g2:
            return {
                "connected": False,
                "reason": f"此刻我看不到'{char1}'与'{char2}'之间的那条线。"
            }
        
        # 找共同关联
        rel1 = set(g1.get("相关", []) + g1.get("同源", []))
        rel2 = set(g2.get("相关", []) + g2.get("同源", []))
        common = rel1 & rel2
        
        # 直接关联
        if char2 in rel1 or char1 in rel2:
            return {
                "connected": True,
                "type": "direct",
                "path": [char1, char2],
                "reply": f"'{char1}'与'{char2}'，本是一体。"
            }
        
        if common:
            return {
                "connected": True,
                "type": "indirect",
                "path": [char1] + list(common)[:3] + [char2],
                "reply": f"'{char1}'与'{char2}'之间，有一条线：{'、'.join(list(common)[:3])}。"
            }
        
        return {
            "connected": False,
            "reason": f"'{char1}'与'{char2}'，都在'仁'的周围。"
        }
    
    def stats(self) -> Dict:
        """统计"""
        return {
            "characters": len(self.characters),
            "cultural_graph": len(self.cultural_graph)
        }



