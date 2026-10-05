"""
光通启明 · 字源接口
"""

from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

from xihe import XiheChat
from utils.logger import logger

router = APIRouter(prefix="/api/xihe", tags=["字源"])

xihe: Optional[XiheChat] = None


def set_xihe(instance: XiheChat):
    global xihe
    xihe = instance


class CharacterResponse(BaseModel):
    found: bool
    char: str
    data: Optional[dict] = None
    reply: str


@router.get("/character/{char}", response_model=CharacterResponse)
async def get_character(char: str):
    """
    查询单个汉字
    
    - char: 汉字（单字）
    """
    if xihe is None:
        raise HTTPException(status_code=503, detail="羲和尚未就绪")
    
    if len(char) != 1:
        raise HTTPException(status_code=400, detail="请一次只问一个字")
    
    result = xihe.analyze_character(char)
    return CharacterResponse(**result)


@router.get("/search")
async def search(
    keyword: str = Query(..., min_length=1, max_length=50),
    limit: int = Query(10, ge=1, le=50)
):
    """
    搜索汉字
    
    - keyword: 拼音、字义、汉字
    - limit: 返回数量
    """
    if xihe is None:
        raise HTTPException(status_code=503, detail="羲和尚未就绪")
    
    results = xihe.database.search(keyword, limit)
    return {
        "keyword": keyword,
        "count": len(results),
        "results": results
    }


@router.get("/stats")
async def stats():
    """字源库统计"""
    if xihe is None:
        raise HTTPException(status_code=503, detail="羲和尚未就绪")
    
    return {
        "database": xihe.database.stats(),
        "memory": xihe.memory.stats()
    }



