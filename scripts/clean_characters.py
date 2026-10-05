#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
光通启明 · 字源库数据清洗脚本
上海易通和维科技有限责任公司
yitonghewei.com

功能：
1. 读取原始 characters_3755.json
2. 补全缺失字段（拼音、部首、笔画、本义等）
3. 自动生成羲和视角
4. 生成部首索引和拼音索引
"""

import json
import random
from pathlib import Path
from pypinyin import pinyin, Style

# ============================================
# 配置
# ============================================
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
INPUT_FILE = PROJECT_ROOT / "docs" / "05_character_database" / "characters_3755.json"
OUTPUT_FILE = PROJECT_ROOT / "docs" / "05_character_database" / "characters_3755_clean.json"
REPORT_FILE = PROJECT_ROOT / "docs" / "05_character_database" / "cleaning_report.json"

# 常用部首表（简化版）
RADICALS = {
    "一": ["一","丁","七","万","三","上","下","不","与"],
    "丨": ["中","串"],
    "丶": ["之","为","义"],
    "丿": ["九","乃","久"],
    "乙": ["乙","了","也"],
    "二": ["二","于","五","云","井","亚"],
    "亻": ["人","仁","他","们","你","作","住","位"],
    "八": ["八","公","六","共","兴"],
    "刀": ["刀","分","切","初","别"],
    "力": ["力","办","加","动","助"],
    "口": ["口","可","古","只","叫","右","号","吃"],
    "囗": ["四","回","国","图","圆"],
    "土": ["土","地","在","场","坐","城"],
    "夕": ["夕","外","多","夜","梦"],
    "大": ["大","天","太","夫","头"],
    "女": ["女","好","如","她","妈","妹"],
    "子": ["子","字","学","孩"],
    "宀": ["家","安","定","宝","室"],
    "山": ["山","出","岛","峰"],
    "川": ["川","州"],
    "工": ["工","左","巧"],
    "己": ["己","已","巴"],
    "巾": ["巾","布","市","师","带"],
    "广": ["广","床","店","府"],
    "心": ["心","必","志","忘","念","想"],
    "戈": ["戈","成","我","战"],
    "手": ["手","打","找","把","看"],
    "日": ["日","旧","时","明","春","是"],
    "月": ["月","有","朋","服","能"],
    "木": ["木","本","来","林","果","树"],
    "水": ["水","永","江","河","海","没"],
    "火": ["火","灯","灰","烧","热"],
    "王": ["王","玉","现","理"],
    "田": ["田","由","电","男","画"],
    "目": ["目","看","眼","睛"],
    "石": ["石","码","破","硬"],
    "禾": ["禾","和","秋","种"],
    "竹": ["竹","笑","笔","等"],
    "米": ["米","类","粉","精"],
    "糸": ["糸","红","级","纪","纸"],
    "耳": ["耳","听","聊"],
    "肉": ["肉","肚","肝","脑"],
    "艹": ["艹","花","草","茶"],
    "虫": ["虫","虽","蚁","蜂"],
    "衣": ["衣","表","被","装"],
    "见": ["见","观","觉"],
    "言": ["言","说","话","语","谁"],
    "贝": ["贝","负","财","货"],
    "走": ["走","起","越","趣"],
    "足": ["足","跑","跳","路"],
    "车": ["车","轮","转","轻"],
    "辶": ["辶","边","过","还","这","道"],
    "金": ["金","银","铁","错"],
    "门": ["门","问","间","闻"],
    "阝": ["阝","那","都","部"],
    "雨": ["雨","雪","雷","零"],
    "食": ["食","饭","饮","饱"],
    "马": ["马","骑","验"],
    "鱼": ["鱼","鲜"],
    "鸟": ["鸟","鸡","鸣"],
}

XIHE_TEMPLATES = [
    "{char}字，{radical}为形，{meaning}为意，你心里也有一个。",
    "{char}字，拆开看，里面藏着你的一个念头。",
    "{char}字，古人在它身上，放进了对世界的理解。今天轮到你放了。",
    "{char}字，像一幅画。你看见了什么？",
    "{char}字，{meaning}。你此刻想起什么？",
]

def get_pinyin(char):
    try:
        result = pinyin(char, style=Style.TONE)
        if result and result[0]:
            return result[0][0]
    except Exception:
        pass
    return "待补充"

def get_radical(char):
    for radical, chars in RADICALS.items():
        if char in chars:
            return radical
    return "待补充"

def generate_xihe_perspective(char, meaning="", radical=""):
    template = random.choice(XIHE_TEMPLATES)
    return template.format(
        char=char,
        meaning=meaning or "一个字",
        radical=radical or "它"
    )

def normalize_entry(entry):
    char = entry.get("汉字") or entry.get("char", "")
    if not char:
        return None

    pinyin_val = entry.get("拼音") or get_pinyin(char)
    radical = entry.get("部首") or get_radical(char)
    meaning = entry.get("本义") or "待补充"
    xihe = entry.get("羲和视角") or generate_xihe_perspective(char, meaning, radical)

    return {
        "char": char,
        "pinyin": pinyin_val,
        "radical": radical,
        "strokes": 0,
        "etymology": {
            "oracle": entry.get("甲骨文", "待补充"),
            "bronze": entry.get("金文", "待补充"),
            "seal": entry.get("小篆", "待补充")
        },
        "meaning": {
            "original": meaning,
            "modern": entry.get("现代常用义", "待补充")
        },
        "cultural_links": entry.get("文化关联", []),
        "xihe_perspective": xihe,
        "source": "cleaned"
    }

def main():
    print("=" * 60)
    print("光通启明 · 数据清洗")
    print("=" * 60)

    # 1. 加载原始数据
    if not INPUT_FILE.exists():
        print(f"❌ 找不到输入文件：{INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"✅ 加载原始数据：{len(data)} 条")

    # 2. 清洗
    cleaned = []
    for entry in data:
        result = normalize_entry(entry)
        if result:
            cleaned.append(result)

    # 3. 保存
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)
    print(f"✅ 已保存清洗数据：{OUTPUT_FILE}")

    # 4. 生成索引
    by_pinyin = {}
    by_radical = {}
    for item in cleaned:
        py = item["pinyin"]
        rad = item["radical"]
        if py != "待补充":
            by_pinyin.setdefault(py, []).append(item["char"])
        if rad != "待补充":
            by_radical.setdefault(rad, []).append(item["char"])

    with open(PROJECT_ROOT / "docs" / "05_character_database" / "pinyin_index.json", "w", encoding="utf-8") as f:
        json.dump({"拼音表": by_pinyin, "统计": {"拼音总数": len(by_pinyin)}}, f, ensure_ascii=False, indent=2)
    
    with open(PROJECT_ROOT / "docs" / "05_character_database" / "radical_index.json", "w", encoding="utf-8") as f:
        json.dump({"部首表": by_radical, "统计": {"部首总数": len(by_radical)}}, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已生成拼音索引：{len(by_pinyin)} 个")
    print(f"✅ 已生成部首索引：{len(by_radical)} 个")
    print("=" * 60)
    print("清洗完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()




