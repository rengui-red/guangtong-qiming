\# 光通启明 · 数据处理脚本



> 上海易通和维科技有限责任公司



\## 用途



清洗、补全、标准化 `characters\_3755.json` 字源库数据。



\## 安装依赖



```bash

pip install -r requirements.txt



运行



python clean\_characters.py



输入

text

docs/05\_character\_database/characters\_3755.json


输出

文件	说明

characters_3755_clean.json	清洗后的完整数据

pinyin_index.json	按拼音索引

radical_index.json	按部首索引

stroke_index.json	按笔画索引

cleaning_report.json	清洗报告


清洗内容

补全拼音：用 pypinyin 自动生成（无声调 + 带声调）

补全部首：从内置部首表匹配

补全笔画：从 Unihan 数据匹配（待集成）

统一格式：所有条目统一为标准 JSON 结构

生成羲和视角：为缺失的字自动生成一句话

生成索引：拼音、部首、笔画三个索引文件

数据结构

清洗后的每个条目：

json
{
  "char": "仁",
  "pinyin": "ren",
  "pinyin_tone": "rén",
  "radical": "亻",
  "strokes": 4,
  "etymology": {
    "oracle": "二人并肩",
    "bronze": "同甲骨文",
    "seal": "二人相依"
  },
  "meaning": {
    "original": "仁爱",
    "modern": "仁义、仁政"
  },
  "cultural_links": ["义", "礼", "智", "信"],
  "xihe_perspective": "仁字，二人之间，本有一根线。",
  "source": "cleaned"
}

后续扩展

集成 Unihan 数据库，补全笔画数

集成汉字字源数据库，补全甲骨文/金文/小篆的真实数据

集成《说文解字》数据库，补全本义

生成文化关联图谱（字与字的关联网络）






