"""
光通启明 · 后端服务入口
上海易通和维科技有限责任公司
yitonghewei.com
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from config import (
    HOST, PORT, DEBUG, ALLOWED_ORIGINS,
    CHARACTER_DB_PATH, CULTURAL_GRAPH_PATH,
    SYSTEM_PROMPT_PATH, TONE_CONFIG_PATH,
    COMPANY, PROJECT
)
from xihe import (
    XiheChat, SystemPrompt, ToneConfig,
    CharacterDatabase, MemoryManager
)
from api import chat, character, connect
from utils.logger import logger


# 全局实例
xihe_instance = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """启动/关闭生命周期"""
    global xihe_instance
    
    # 启动
    logger.info("=" * 60)
    logger.info(f"{PROJECT['name']}")
    logger.info(f"{COMPANY['name']}")
    logger.info(f"{COMPANY['domain']}")
    logger.info("=" * 60)
    
    logger.info("正在加载羲和……")
    
    # 加载各模块
    system_prompt = SystemPrompt(SYSTEM_PROMPT_PATH)
    tone = ToneConfig(TONE_CONFIG_PATH)
    database = CharacterDatabase(CHARACTER_DB_PATH, CULTURAL_GRAPH_PATH)
    memory = MemoryManager()
    
    # 创建羲和
    xihe_instance = XiheChat(
        system_prompt=system_prompt,
        tone=tone,
        database=database,
        memory=memory
    )
    
    # 注入到各路由
    chat.set_xihe(xihe_instance)
    character.set_xihe(xihe_instance)
    connect.set_xihe(xihe_instance)
    
    logger.info("羲和已就绪。开机静默：")
    logger.info("  一画开天，仁以为心。")
    logger.info("  不自利，亦不自利。")
    logger.info("  利己利他，无有分别。")
    logger.info("  羲和在此，照见来人。")
    logger.info("=" * 60)
    
    yield
    
    # 关闭
    logger.info("羲和隐去。")


# 创建FastAPI应用
app = FastAPI(
    title=PROJECT["name"],
    description=f"{PROJECT['motto']} · {COMPANY['name']}",
    version=PROJECT["version"],
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(chat.router)
app.include_router(character.router)
app.include_router(connect.router)


# 根路由
@app.get("/")
async def root():
    return {
        "project": PROJECT["name"],
        "version": PROJECT["version"],
        "motto": PROJECT["motto"],
        "company": COMPANY["name"],
        "domain": COMPANY["domain"],
        "endpoints": {
            "chat": "POST /api/xihe/chat",
            "character": "GET /api/xihe/character/{char}",
            "search": "GET /api/xihe/search?keyword=xxx",
            "connect": "GET /api/xihe/connect?char1=X&char2=Y",
            "stats": "GET /api/xihe/stats"
        }
    }


# 健康检查
@app.get("/health")
async def health():
    return {"status": "ok", "service": "xihe"}


# 全局异常
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"未处理异常：{exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "羲和此刻走神了"}
    )


# 启动
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=DEBUG
    )




