"""
光通启明 · 后端配置
上海易通和维科技有限责任公司
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# 加载 .env
load_dotenv()

# 基础路径
BASE_DIR = Path(__file__).resolve().parent

# 大模型配置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
MODEL_NAME = os.getenv("MODEL_NAME", "deepseek-chat")

# 服务配置
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# 路径配置
DOCS_PATH = BASE_DIR / os.getenv("DOCS_PATH", "../docs")
CHARACTER_DB_PATH = BASE_DIR / os.getenv("CHARACTER_DB", "../docs/05_character_database/characters_3755.json")
CULTURAL_GRAPH_PATH = BASE_DIR / os.getenv("CULTURAL_GRAPH", "../docs/05_character_database/cultural_connection_graph.json")
SYSTEM_PROMPT_PATH = BASE_DIR / os.getenv("SYSTEM_PROMPT", "../docs/06_xihe_ai/core/system_prompt.md")
TONE_CONFIG_PATH = BASE_DIR / os.getenv("TONE_CONFIG", "../docs/06_xihe_ai/tone/tone_config.json")

# CORS
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# 公司信息
COMPANY = {
    "name": "上海易通和维科技有限责任公司",
    "name_en": "Shanghai Yitonghewei Technology Co., Ltd.",
    "domain": "yitonghewei.com",
    "email_contact": "contact@yitonghewei.com",
    "email_support": "support@yitonghewei.com"
}

# 项目信息
PROJECT = {
    "name": "光通启明 · 汉字光宇世界",
    "name_en": "Guangtong Qiming · The Hanzi Light Universe",
    "version": "1.0.0",
    "motto": "一画开天，仁以为心"
}




