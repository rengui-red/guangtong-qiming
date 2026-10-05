#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
光通启明 · 项目功能测试（体检脚本）
"""
import json
from pathlib import Path
import random

DATA_DIR = Path(__file__).resolve().parent  / "data"

FINAL_FILE = DATA_DIR / "final" / "characters_3755_clean.json"
REPORT_FILE = DATA_DIR / "final" / "build_report.json"

def test_project():
    print("=" * 50)
    print("   光通启明 · 数据库功能测试报告")
    print("=" * 50)

    if not FINAL_FILE.exists():
        print("❌ 未找到最终数据库文件！请先运行合并脚本。")
        return

    try:
        with open(FINAL_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ 读取数据库失败：{e}")
        return

    total = len(data)
    print(f"📊 基础统计：共 {total} 个汉字\n")

    # 统计各字段完整度
    stats = {
        "拼音": sum(1 for x in data if x.get("pinyin")),
        "部首": sum(1 for x in data if x.get("radical")),
        "笔画": sum(1 for x in data if x.get("strokes")),
        "字义": sum(1 for x in data if x.get("meaning")),
        "字形图片": sum(1 for x in data if x.get("glyph_images")),
        "字源(甲骨文/金文/小篆)": sum(1 for x in data if x.get("oracle") or x.get("bronze") or x.get("seal"))
    }

    for k, v in stats.items():
        percent = (v / total) * 100
        status = "✅ 优秀" if percent >= 90 else ("⚠️ 待补充" if percent > 0 else "❌ 缺失")
        print(f"  - {k}: {v} / {total} ({percent:.1f}%) {status}")

    print("\n" + "=" * 50)
    print("   🔍 随机抽样验货（抽查3个字）")
    print("=" * 50)

    samples = random.sample(data, 3)
    for s in samples:
        print(f"\n【{s['char']}】")
        print(f"  拼音：{s.get('pinyin', '无')}")
        print(f"  部首：{s.get('radical', '无')}  |  笔画：{s.get('strokes', 0)}")
        print(f"  字义：{(s.get('meaning', '无')[:50] + '...') if s.get('meaning') else '无'}")
        glyphs = s.get('glyph_images', [])
        print(f"  字形图片：{len(glyphs)} 张")
        if glyphs:
            print(f"    示例链接：{glyphs[0]}")

    print("\n" + "=" * 50)
    print("   💡 测试结论与下一步建议")
    print("=" * 50)
    
    if stats["字义"] == 0:
        print("  [警告] 字义数据全空。大概率是爬虫遭遇了汉典网的反爬拦截。")
        print("  [建议] 放弃爬虫，转为使用本地字源数据集，或使用AI批量生成字义后手动补全。")
    else:
        print("  [成功] 字义数据已成功入库，可以进入下一步前端开发或AI训练。")
    
    if stats["部首"] < total:
        print(f"  [提示] 有 {total - stats['部首']} 个字缺少部首信息（可能是Unihan库未收录的罕见异体字），建议后续手动补录。")

if __name__ == "__main__":
    test_project()



