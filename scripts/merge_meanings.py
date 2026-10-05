import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FINAL_FILE = SCRIPT_DIR / "data" / "final" / "characters_3755_clean.json"
WORD_FILE = SCRIPT_DIR / "word.json"

if not WORD_FILE.exists():
    print("❌ 找不到 word.json")
    exit()
if not FINAL_FILE.exists():
    print("❌ 找不到 characters_3755_clean.json")
    exit()

print("正在读取 26MB 的大字典，请稍等 (大概需要5-10秒)...")
with open(WORD_FILE, "r", encoding="utf-8") as f:
    word_data = json.load(f)

print("正在读取数据库文件...")
with open(FINAL_FILE, "r", encoding="utf-8") as f:
    target_data = json.load(f)

meaning_dict = {}
for item in word_data:
    w = item.get("word")
    e = item.get("explanation")
    # 只提取单个汉字，忽略词语
    if w and e and len(w) == 1:
        meaning_dict[w] = e

updated_count = 0
for char_info in target_data:
    char = char_info.get("char")
    if char in meaning_dict:
        char_info["meaning"] = meaning_dict[char]
        updated_count += 1

print("正在写回文件...")
with open(FINAL_FILE, "w", encoding="utf-8") as f:
    json.dump(target_data, f, ensure_ascii=False, indent=2)

print(f"✅ 合并完成！一共为 {updated_count} 个汉字补充了字义！")




