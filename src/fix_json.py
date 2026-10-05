import json

# 读取你的3.9MB数据
with open("characters_3755.json", "r", encoding="utf-8") as f:
    data = json.load(f)

new_data = []
for item in data:
    # 把英文名翻译成前端要的中文名
    new_item = {
        "汉字": item.get("char", ""),
        "拼音": item.get("pinyin", ""),
        "甲骨文": item.get("oracle", ""), # 图片这块原本就是空的
        "本义": item.get("meaning", "暂无释义"),
        "羲和视角": item.get("meaning", "暂无视角") # 暂时用字义顶替视角
    }
    new_data.append(new_item)

# 覆盖原文件
with open("characters_3755.json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)

print("✅ 数据格式转换成功！现在去刷新网页吧！")