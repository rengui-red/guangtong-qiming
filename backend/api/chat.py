"""
光通启明 · 对话接口
"""

from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

from xihe import XiheChat
from utils.logger import logger

router = APIRouter(prefix="/api/xihe", tags=["羲和对话"])

# 全局羲和实例（在 main.py 中注入）
xihe: Optional[XiheChat] = None


def set_xihe(instance: XiheChat):
    """注入羲和实例"""
    global xihe
    xihe = instance


class ChatRequest(BaseModel):
    message: str = Field(..., description="用户消息", min_length=1, max_length=2000)
    user_id: str = Field("anonymous", description="用户ID")


class ChatResponse(BaseModel):
    reply: str = Field(..., description="羲和的回应")
    char_analyzed: Optional[str] = Field(None, description="分析的字")
    references: List[str] = Field(default_factory=list, description="引用的字")


@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """
    与羲和对话
    
    - message: 用户说的话
    - user_id: 用户标识（可选）
    """
    if xihe is None:
        raise HTTPException(status_code=503, detail="羲和尚未就绪")
    
    try:
        result = xihe.chat(req.message, req.user_id)
        return ChatResponse(**result)
    except Exception as e:
        logger.error(f"对话失败：{e}")
        raise HTTPException(status_code=500, detail="羲和此刻走神了")