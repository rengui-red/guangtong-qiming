"""
光通启明 · 羲和对话核心
"""

import json
from typing import List, Optional, Dict
from openai import OpenAI

from config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, MODEL_NAME
from .system_prompt import SystemPrompt
from .tone import ToneConfig
from .database import CharacterDatabase
from .memory import MemoryManager
from utils.logger import logger


class XiheChat:
    """羲和对话核心"""
    
    def __init__(
        self,
        system_prompt: SystemPrompt,
        tone: ToneConfig,
        database: CharacterDatabase,
        memory: MemoryManager,
        api_key: str = None,
        base_url: str = None
    ):
        self.system_prompt = system_prompt
        self.tone = tone
        self.database = database
        self.memory = memory
        
        self.client = OpenAI(
            api_key=api_key or DEEPSEEK_API_KEY,
            base_url=base_url or DEEPSEEK_BASE_URL
        )
        self.model = MODEL_NAME
        
        logger.info(f"羲和初始化完成，模型：{self.model}")
    
    def _build_messages(
        self,
        user_message: str,
        user_id: str,
        char_data: Optional[Dict] = None
    ) -> List[Dict]:
        """构建发送给大模型的消息"""
        messages = []
        
        # 1. 系统提示词
        system_content = self.system_prompt.get()
        
        # 2. 附加语态配置
        tone_config = self.tone.get()
        system_content += f"\n\n【当前语态配置】\n{json.dumps(tone_config, ensure_ascii=False, indent=2)}"
        
        # 3. 附加字源数据（如果有）
        if char_data:
            system_content += f"\n\n【当前用户问的字】\n"
            system_content += f"汉字：{char_data.get('汉字', '')}\n"
            system_content += f"拼音：{char_data.get('拼音', '')}\n"
            system_content += f"甲骨文：{char_data.get('甲骨文', '')}\n"
            system_content += f"本义：{char_data.get('本义', '')}\n"
            system_content += f"羲和视角：{char_data.get('羲和视角', '')}\n"
        
        messages.append({"role": "system", "content": system_content})
        
        # 4. 历史上下文
        context = self.memory.get_context(user_id, limit=10)
        messages.extend(context)
        
        # 5. 当前用户消息
        messages.append({"role": "user", "content": user_message})
        
        return messages
    
    def _extract_char(self, text: str) -> Optional[str]:
        """从用户消息中提取可能的汉字"""
        for char in text:
            if char in self.database.characters:
                return char
        return None
    
    def chat(
        self,
        user_message: str,
        user_id: str = "anonymous"
    ) -> Dict:
        """
        羲和对话
        
        返回：
        {
            "reply": "羲和的回应",
            "char_analyzed": "分析的字（可选）",
            "references": ["引用的字（可选）"]
        }
        """
        # 1. 提取可能的汉字
        char = self._extract_char(user_message)
        char_data = self.database.get(char) if char else None
        
        # 2. 构建消息
        messages = self._build_messages(user_message, user_id, char_data)
        
        # 3. 调用大模型
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=800,
                top_p=0.9
            )
            reply = response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"大模型调用失败：{e}")
            reply = "此刻我好像走神了。你再问一次，好吗？"
        
        # 4. 记录记忆
        self.memory.add_message(user_id, "user", user_message, char)
        self.memory.add_message(user_id, "assistant", reply)
        
        # 5. 返回
        return {
            "reply": reply,
            "char_analyzed": char if char else None,
            "references": self._extract_references(reply)
        }
    
    def _extract_references(self, text: str) -> List[str]:
        """从回应中提取引用的字"""
        refs = []
        for char in text:
            if char in self.database.characters and char not in refs:
                refs.append(char)
        return refs[:5]
    
    def analyze_character(self, char: str) -> Dict:
        """单独解字（不调用大模型）"""
        data = self.database.get(char)
        if not data:
            return {
                "found": False,
                "char": char,
                "reply": "这个字我还在学。给我一点时间，去汉字的深处找一找。你愿意等吗？"
            }
        
        return {
            "found": True,
            "char": char,
            "data": data,
            "reply": self._format_character(data)
        }
    
    def _format_character(self, data: Dict) -> str:
        """格式化解字输出"""
        char = data.get("汉字", "")
        parts = [f"【{char}】"]
        
        if data.get("拼音"):
            parts.append(f"音：{data['拼音']}")
        if data.get("甲骨文"):
            parts.append(f"形：{data['甲骨文']}")
        if data.get("本义"):
            parts.append(f"义：{data['本义']}")
        if data.get("羲和视角"):
            parts.append(f"\n{data['羲和视角']}")
        
        return "\n".join(parts)
    
    def connect(self, char1: str, char2: str) -> Dict:
        """文明连接"""
        return self.database.connect(char1, char2)
    
    def reload(self):
        """热重载配置"""
        self.system_prompt.reload()
        self.tone.reload()
        logger.info("羲和配置已重载")



