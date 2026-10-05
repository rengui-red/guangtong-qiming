\# 字源库 · 说明文档



> 光通启明 · 数据层核心

> 上海易通和维科技有限责任公司

> yitonghewei.com



\---



\## 一、这是什么？



\*\*字源库\*\*，是「光通启明」项目的\*\*数字基因库\*\*。



它把每一个汉字，从甲骨文到楷书的三千年历程，用结构化数据记录下来。



\*\*它是羲和的眼睛，也是羲和的记忆。\*\*



\---



\## 二、目录内容



docs/05\_character\_database/

│

├── README.md ← 本文件

├── characters\_3755.json ← 主数据（3755字）

├── characters\_3755\_clean.json ← 清洗后的数据（运行脚本后生成）

├── radical\_index.json ← 部首索引

├── pinyin\_index.json ← 拼音索引

├── stroke\_index.json ← 笔画索引

├── cultural\_connection\_graph.json ← 文化关联图谱

├── xihe\_perspectives.json ← 羲和视角库

└── build\_report.json ← 数据构建报告





\---



\## 三、主数据结构



\### 3.1 `characters\_3755.json`



\*\*格式：\*\* JSON 数组



\*\*示例条目：\*\*



```json

{

&#x20; "汉字": "仁",

&#x20; "拼音": "rén",

&#x20; "拼音带声调": "rén",

&#x20; "部首": "亻",

&#x20; "笔画": 4,

&#x20; "甲骨文": "二人并肩",

&#x20; "金文": "同甲骨文",

&#x20; "小篆": "二人相依",

&#x20; "本义": "仁爱",

&#x20; "现代常用义": "仁义、仁政",

&#x20; "文化关联": \["义", "礼", "智", "信"],

&#x20; "羲和视角": "仁，二人之间，本有一根线。"

}



{

&#x20; "char": "仁",

&#x20; "pinyin": "ren",

&#x20; "pinyin\_tone": "rén",

&#x20; "radical": "亻",

&#x20; "strokes": 4,

&#x20; "etymology": {

&#x20;   "oracle": "二人并肩",

&#x20;   "bronze": "同甲骨文",

&#x20;   "seal": "二人相依"

&#x20; },

&#x20; "meaning": {

&#x20;   "original": "仁爱",

&#x20;   "modern": "仁义、仁政"

&#x20; },

&#x20; "cultural\_links": \["义", "礼", "智", "信"],

&#x20; "xihe\_perspective": "仁，二人之间，本有一根线。",

&#x20; "source": "cleaned"

}













