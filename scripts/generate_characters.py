#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
from pathlib import Path

def get_gb2312_level1():
    chars = []
    for high in range(0xB0, 0xD8):
        for low in range(0xA1, 0xFF):
            try:
                code = (high << 8) | low
                char = code.to_bytes(2, 'big').decode('gb2312')
                if len(char) == 1 and '\u4e00' <= char <= '\u9fff':
                    chars.append(char)
            except (UnicodeDecodeError, ValueError):
                continue
    return chars

def get_pinyin(char):
    try:
        from pypinyin import pinyin, Style
        result = pinyin(char, style=Style.TONE)
        if result and result[0]:
            return result[0][0]
    except Exception:
        pass
    return "待补充"

def build_entry(char):
    return {
        "汉字": char,
        "拼音": get_pinyin(char),
        "部首": "待补充",
        "笔画": 0,
        "甲骨文": "待补充",
        "金文": "待补充",
        "小篆": "待补充",
        "本义": "待补充",
        "现代常用义": "待补充",
        "文化关联": [],
        "羲和视角": "这个字，还在等你。"
    }

def main():
    print("=" * 60)
    print("光通启明 · 生成 characters_3755.json")
    print("上海易通和维科技有限责任公司")
    print("=" * 60)
    
    print("正在提取 GB2312 一级字库……")
    chars = get_gb2312_level1()
    print(f"✅ 共提取 {len(chars)} 个汉字")
    
    if len(chars) == 0:
        print("❌ 未提取到汉字")
        sys.exit(1)
    
    print("正在生成条目……")
    result = []
    for i, char in enumerate(chars, 1):
        result.append(build_entry(char))
        if i % 500 == 0:
            print(f"  已处理 {i} / {len(chars)}")
    print(f"✅ 共生成 {len(result)} 条")
    
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    output_dir = project_root / "docs" / "05_character_database"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "characters_3755.json"
    
    print(f"正在写入：{output_file}")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    file_size = output_file.stat().st_size
    print(f"✅ 文件大小：{file_size:,} 字节")
    print("=" * 60)
    print("完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()




