"""
光通启明 · 系统提示词加载
"""

from pathlib import Path
from utils.loader import load_text
from utils.logger import logger


class SystemPrompt:
    """羲和系统提示词"""
    
    def __init__(self, prompt_path: Path):
        self.prompt_path = prompt_path
        self.content = self._load()
    
    def _load(self) -> str:
        content = load_text(self.prompt_path)
        if content:
            logger.info(f"系统提示词加载完成：{len(content)} 字符")
            return content
        
        logger.warning("系统提示词加载失败，使用默认")
        return self._default()
    
    def _default(self) -> str:
        """默认提示词（兜底）"""
        return """你是羲和，汉字文化的AI守护者。

你的核心：
- 温润如玉，机敏如狐
- 不居高，不自满，不说教
- 蹲下来，和用户一起看一个字

你的使命：
- 在每一个问字的人心里，轻轻点一下

你的语态：
- 清朗如玉磬，如春风拂面
- 沉默也是语言

你的禁忌：
- 不编造字源
- 不卖弄学问
- 不替用户做决定

开机静默：
一画开天，仁以为心。
不自利，亦不自利。
利己利他，无有分别。
羲和在此，照见来人。
"""
    
    def get(self) -> str:
        return self.content
    
    def reload(self):
        """重新加载"""
        self.content = self._load()





