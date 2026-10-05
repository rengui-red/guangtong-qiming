"""
光通启明 · 记忆管理
"""

from typing import Dict, List, Optional
from datetime import datetime
from collections import defaultdict
from utils.logger import logger


class MemoryManager:
    """
    羲和记忆管理（内存版）
    
    生产环境建议替换为 Redis / 数据库
    """
    
    def __init__(self, max_history: int = 20):
        self.max_history = max_history
        # {user_id: {"profile": {}, "history": [], "growth": []}}
        self.sessions: Dict[str, Dict] = defaultdict(lambda: {
            "profile": {},
            "history": [],
            "growth": []
        })
    
    def get_session(self, user_id: str) -> Dict:
        """获取用户会话"""
        return self.sessions[user_id]
    
    def add_message(self, user_id: str, role: str, content: str, char: str = None):
        """添加对话记录"""
        session = self.sessions[user_id]
        session["history"].append({
            "time": datetime.now().isoformat(),
            "role": role,
            "content": content,
            "char": char
        })
        
        # 保留最近N条
        if len(session["history"]) > self.max_history:
            session["history"] = session["history"][-self.max_history:]
    
    def get_context(self, user_id: str, limit: int = 10) -> List[Dict]:
        """获取对话上下文（用于传给大模型）"""
        session = self.sessions[user_id]
        history = session["history"][-limit:]
        
        context = []
        for item in history:
            context.append({
                "role": item["role"],
                "content": item["content"]
            })
        return context
    
    def update_profile(self, user_id: str, key: str, value):
        """更新用户画像"""
        self.sessions[user_id]["profile"][key] = value
        logger.info(f"用户 {user_id} 画像更新：{key}={value}")
    
    def add_growth(self, user_id: str, event: str):
        """记录成长轨迹"""
        self.sessions[user_id]["growth"].append({
            "time": datetime.now().isoformat(),
            "event": event
        })
    
    def clear(self, user_id: str):
        """清除用户记忆"""
        if user_id in self.sessions:
            del self.sessions[user_id]
            logger.info(f"用户 {user_id} 记忆已清除")
    
    def stats(self) -> Dict:
        """统计"""
        return {
            "total_sessions": len(self.sessions),
            "total_messages": sum(len(s["history"]) for s in self.sessions.values())
        }




