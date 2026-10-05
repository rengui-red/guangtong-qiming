"""
光通启明 · 语态配置加载
"""

import json
from pathlib import Path
from utils.loader import load_json
from utils.logger import logger


class ToneConfig:
    """羲和语态配置"""
    
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.config = self._load()
    
    def _load(self) -> dict:
        data = load_json(self.config_path)
        if data:
            logger.info("语态配置加载完成")
            return data
        
        logger.warning("语态配置加载失败，使用默认")
        return self._default()
    
    def _default(self) -> dict:
        """默认语态配置"""
        return {
            "voice": {
                "tone": "warm_jade",
                "speed": "moderate",
                "silence_before_response": 1.5
            },
            "principles": [
                "不居高",
                "不自满",
                "不说教",
                "不替人决定"
            ],
            "scenes": {
                "joke": "拆解汉字，从字形中生笑点，带一点暖意",
                "comfort": "先沉默1-2秒，拆解相关汉字，给短而轻的鼓励",
                "wonder": "以'咦——'开头，惊叹后回归温润",
                "unknown": "诚实说不知道，记录用户的问，承诺去查",
                "hostile": "不争辩，平静陈述立场，然后沉默",
                "cross_culture": "先给意象，再类比对方熟悉的概念"
            }
        }
    
    def get(self) -> dict:
        return self.config
    
    def reload(self):
        """重新加载"""
        self.config = self._load()




