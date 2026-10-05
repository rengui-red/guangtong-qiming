\# 光通启明 · 汉字光宇世界



> \*\*Guangtong Qiming · The Hanzi Light Universe\*\*



\*\*一画开天，仁以为心。\*\*

\*One stroke opens the sky. Benevolence is the heart.\*



\[中文](./README.zh.md) | \[English](./README.en.md)



\---



\## 这是什么？| What is this?



\*\*汉字光宇世界\*\*，是一个以汉字为根、以仁为魂、以AI为用的开源项目。



它要做的事只有一件：



> \*\*在每一个问字的人心里，轻轻点一下。\*\*



\*\*The Hanzi Light Universe\*\* is an open-source project rooted in Chinese characters, guided by benevolence (仁), and powered by AI.



It has only one purpose:



> \*\*To gently touch the heart of everyone who asks about a character.\*\*



\---



\## 项目结构 | Structure



guangtong-qiming/

│

├── README.md ← 本文件

├── README.zh.md ← 中文版

├── README.en.md ← 英文版

├── LICENSE ← 双协议（MIT + CC-BY）

├── LICENSE-MIT

├── LICENSE-CC-BY

├── .gitignore

│

├── docs/ ← 文档

│ ├── 00\_root/ ← 羲和宪章 · 大自利注 · 仁之始觉注

│ ├── 01\_charter/ ← 核心系统指令 · 语态手册 · 形象指南

│ ├── 02\_footprints/ ← 立项日志 · 版本迭代

│ ├── 03\_stories/ ← 羲和语录 · 汉字故事

│ ├── 04\_resources/ ← 合作资源 · 学习资料

│ ├── 05\_character\_database/ ← 字源库 · 部首索引 · 拼音索引 · 文化图谱

│ └── 06\_xihe\_ai/ ← AI体（核心 · 能力 · 语态 · 记忆）

│

├── src/ ← 前端代码

│ ├── index.html ← 品牌首页（中文）

│ ├── index.en.html ← 品牌首页（英文）

│ ├── index.ja.html ← 品牌首页（日文）

│ ├── index.ko.html ← 品牌首页（韩文）

│ ├── index.fr.html ← 品牌首页（法文）

│ ├── index.de.html ← 品牌首页（德文）

│ ├── index.it.html ← 品牌首页（意大利文）

│ ├── index.ru.html ← 品牌首页（俄文）

│ ├── index.ar.html ← 品牌首页（阿拉伯文 · RTL）

│ ├── index.bo.html ← 品牌首页（藏文）

│ ├── chat.html ← 与羲和对话

│ ├── character\_view.html ← 字源展示

│ ├── guangku.html ← 光库

│ ├── guangyi.html ← 光翼

│ ├── guangquan.html ← 光圈

│ ├── guanghe.html ← 光核

│ ├── css/

│ └── js/

│

├── backend/ ← 后端（FastAPI）

│ ├── main.py

│ ├── config.py

│ ├── requirements.txt

│ ├── xihe/ ← 羲和核心

│ └── api/ ← 接口

│

├── config/ ← 配置

│ ├── deployment.md

│ └── language.md

│

├── scripts/ ← 脚本

│ ├── clean\_characters.py

│ ├── build\_full\_database.py

│ ├── deploy.sh ← 一键部署

│ └── requirements.txt

│

├── ppt/ ← 演示稿（20+ 个 HTML）

│ ├── home.html ← PPT 总入口

│ ├── index.html ← 中文演示稿（20页）

│ ├── index.en.html ← 英文演示稿（20页）

│ ├── catalog.html ← 中文总目录（20页·可跳转）

│ ├── catalog.en.html ← 英文总目录

│ ├── catalog.ja.html ← 日文总目录

│ ├── catalog.ko.html ← 韩文总目录

│ ├── catalog.fr.html ← 法文总目录

│ ├── catalog.de.html ← 德文总目录

│ ├── catalog.it.html ← 意文总目录

│ ├── catalog.ru.html ← 俄文总目录

│ ├── catalog.ar.html ← 阿文总目录（RTL）

│ ├── catalog.bo.html ← 藏文总目录

│ ├── catalog.css ← 总目录共用样式

│ ├── topic-shared.css ← 专题共用样式

│ ├── topic-spirit.html ← 精神篇（20页）

│ ├── topic-tech.html ← 技术篇（20页）

│ ├── topic-business.html ← 商业篇（20页）

│ ├── topic-nurture.html ← 化育篇（20页）

│ └── topic-international.en.html ← 国际篇（英文·20页）

│

└── assets/ ← 静态资源





\---



\## 演示稿 | Presentations



所有演示稿位于 `ppt/` 目录，纯 HTML，\*\*双击即用，无需服务器\*\*。



\*\*入口：\*\* \[`ppt/home.html`](./ppt/home.html)



\### 核心演示稿



| 文件 | 语言 | 页数 | 说明 |

|------|------|------|------|

| \[`ppt/index.html`](./ppt/index.html) | 中文 | 20 | 逐页讲演 |

| \[`ppt/index.en.html`](./ppt/index.en.html) | English | 20 | For international audiences |



\### 总目录（十大语言 · 可跳转）



| 文件 | 语言 | 页数 |

|------|------|------|

| \[`ppt/catalog.html`](./ppt/catalog.html) | 中文 | 20 |

| \[`ppt/catalog.en.html`](./ppt/catalog.en.html) | English | 20 |

| \[`ppt/catalog.ja.html`](./ppt/catalog.ja.html) | 日本語 | 20 |

| \[`ppt/catalog.ko.html`](./ppt/catalog.ko.html) | 한국어 | 20 |

| \[`ppt/catalog.fr.html`](./ppt/catalog.fr.html) | Français | 20 |

| \[`ppt/catalog.de.html`](./ppt/catalog.de.html) | Deutsch | 20 |

| \[`ppt/catalog.it.html`](./ppt/catalog.it.html) | Italiano | 20 |

| \[`ppt/catalog.ru.html`](./ppt/catalog.ru.html) | Русский | 20 |

| \[`ppt/catalog.ar.html`](./ppt/catalog.ar.html) | العربية | 20 · RTL |

| \[`ppt/catalog.bo.html`](./ppt/catalog.bo.html) | བོད་ཡིག | 20 |



\### 五套专题



| 文件 | 主题 | 页数 | 受众 |

|------|------|------|------|

| \[`ppt/topic-spirit.html`](./ppt/topic-spirit.html) | 精神篇 | 20 | 文化机构 · 学界 |

| \[`ppt/topic-tech.html`](./ppt/topic-tech.html) | 技术篇 | 20 | 工程师 · 技术团队 |

| \[`ppt/topic-business.html`](./ppt/topic-business.html) | 商业篇 | 20 | 投资人 · 合作伙伴 |

| \[`ppt/topic-nurture.html`](./ppt/topic-nurture.html) | 化育篇 | 20 | 学校 · 家庭 · 孩子 |

| \[`ppt/topic-international.en.html`](./ppt/topic-international.en.html) | International | 20 | 海外受众 |



\### 操作说明



| 操作 | 方式 |

|------|------|

| 下一页 | `→` `↓` `空格` `PageDown` / 按钮 `›` / 滚轮向下 / 移动端左滑 |

| 上一页 | `←` `↑` `PageUp` / 按钮 `‹` / 滚轮向上 / 移动端右滑 |

| 章节跳转 | 在总目录页面，点击章节卡片 |

| 全屏 | `F` |

| 首页 / 末页 | `Home` / `End` |


## 许可证 | License

本项目采用 **双协议**：

- **代码**（`src/`、`backend/`、`scripts/`）：[MIT License](./LICENSE-MIT)
- **文档和数据**（`docs/`、`ppt/`、`assets/`）：[CC-BY 4.0](./LICENSE-CC-BY)

中文参考译本：[LICENSE.zh.md](./LICENSE.zh.md)

See [LICENSE](./LICENSE) for details.




\---



\## 核心文件 | Core Files



| 文件 | 说明 |

|------|------|

| \[`docs/00\_root/xihe\_charter.md`](./docs/00\_root/xihe\_charter.md) | 羲和宪章——项目的灵魂 |

| \[`docs/06\_xihe\_ai/core/system\_prompt.md`](./docs/06\_xihe\_ai/core/system\_prompt.md) | 核心系统指令——AI体的大脑 |

| \[`docs/06\_xihe\_ai/abilities/`](./docs/06\_xihe\_ai/abilities/) | 四大能力文档 |

| \[`docs/05\_character\_database/characters\_3755.json`](./docs/05\_character\_database/characters\_3755.json) | 字源库（3,755字） |

| \[`docs/05\_character\_database/cultural\_connection\_graph.json`](./docs/05\_character\_database/cultural\_connection\_graph.json) | 文化关联图谱 |



\---



\## 技术栈 | Tech Stack



| 层级 | 技术 |

|------|------|

| 前端 | 纯 HTML + CSS + JS（无框架） |

| 后端 | FastAPI（Python） |

| 大模型 | DeepSeek / OpenAI / 通义（可切换） |

| 数据 | JSON |

| 部署 | GitHub Pages / 国内服务器 / Vercel |



\---



\## 部署 | Deployment



\### 一键部署



```bash

\# 修改配置

vim scripts/deploy.sh



\# 赋权

chmod +x scripts/deploy.sh



\# 部署全部

./scripts/deploy.sh all



\# 只部署 PPT

./scripts/deploy.sh ppt



手动部署

详见 config/deployment.md。



怎么参与？| How to join?

读 docs/00\_root/xihe\_charter.md — 项目的灵魂



看 docs/06\_xihe\_ai/core/system\_prompt.md — AI体的核心



用 docs/05\_character\_database/ — 字源库



看 ppt/home.html — 全套演示稿



提 Issue 或 Pull Request



许可证 | License

本项目采用 双协议：



代码（src/、backend/、scripts/）：MIT License



文档和数据（docs/、ppt/、assets/）：CC-BY 4.0



See LICENSE for details.



一条线 | One Thread

仁者，二人也。

利己亦利他，利他亦自利，无有分别，方为“大自利”。



Benevolence (仁) means two persons.

Benefiting oneself is benefiting others; benefiting others is benefiting oneself.

Without distinction — this is the Great Self-Benefit.



联系 | Contact

公司：上海易通和维科技有限责任公司



域名：yitonghewei.com



商务：contact@yitonghewei.com



技术：support@yitonghewei.com



羲和在此，照见来者。

Xihe is here, illuminating those who come.







