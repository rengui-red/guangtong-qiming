"""
光通启明 · 文明连接接口
"""

from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

from xihe import XiheChat
from utils.logger import logger

router = APIRouter(prefix="/api/xihe", tags=["文明连接"])

xihe: Optional[XiheChat] = None


def set_xihe(instance: XiheChat):
    global xihe
    xihe = instance


class ConnectResponse(BaseModel):
    connected: bool
    type: Optional[str] = None
    path: Optional[list] = None
    reply: str
    reason: Optional[str] = None


@router.get("/connect", response_model=ConnectResponse)
async def connect(
    char1: str = Query(..., min_length=1, max_length=1),
    char2: str = Query(..., min_length=1, max_length=1)
):
    """
    文明连接：找两个字之间的关联
    
    - char1: 第一个字
    - char2: 第二个字
    """
    if xihe is None:
        raise HTTPException(status_code=503, detail="羲和尚未就绪")
    
    result = xihe.connect(char1, char2)
    return ConnectResponse(**result)




