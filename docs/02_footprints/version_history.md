\# 光通启明 · 版本迭代



> 记录每一次版本更新的具体内容

> 上海易通和维科技有限责任公司



\---



\## 版本规范



采用 \*\*语义化版本\*\* 规范：



主版本.次版本.修订号

↑ ↑ ↑

重大 功能 修复





\- \*\*主版本\*\*：不兼容的重大变更

\- \*\*次版本\*\*：向下兼容的功能新增

\- \*\*修订号\*\*：向下兼容的问题修复



\---



\## v1.0.0 · 2026-04-16



\### 主题



\*\*奠基 · 精神骨架完成\*\*



\### 新增



\#### 文档

\- `docs/00\_root/xihe\_charter.md` — 羲和宪章

\- `docs/00\_root/great\_self\_benefit.md` — 大自利注

\- `docs/00\_root/benevolence\_awakening.md` — 仁之始觉注

\- `docs/01\_charter/core\_system\_prompt.md` — 核心系统指令

\- `docs/01\_charter/tone\_manual.md` — 语态手册

\- `docs/01\_charter/image\_guide.md` — 形象指南

\- `docs/01\_charter/taboos.md` — 交互禁忌



\#### 数据

\- `docs/05\_character\_database/characters\_3755.json` — 3,755字源库骨架

\- `docs/05\_character\_database/radical\_index.json` — 部首索引

\- `docs/05\_character\_database/pinyin\_index.json` — 拼音索引

\- `docs/05\_character\_database/cultural\_connection\_graph.json` — 文化关联图谱（200字）



\#### 配置

\- `LICENSE` — 双协议声明

\- `LICENSE-MIT`

\- `LICENSE-CC-BY`

\- `.gitignore`



\### 说明



这是第一个正式版本。

精神骨架完成。



\*\*从「一个字」到「一个系统」，用了 34 天。\*\*



\---



\## v1.1.0 · 2026-05-01



\### 主题



\*\*前端 · 十种语言版本\*\*



\### 新增



\#### 前端页面

\- `src/index.html` — 品牌首页（中文）

\- `src/index.en.html` — 品牌首页（英文）

\- `src/index.fr.html` — 品牌首页（法文）

\- `src/index.de.html` — 品牌首页（德文）

\- `src/index.it.html` — 品牌首页（意大利文）

\- `src/index.ja.html` — 品牌首页（日文）

\- `src/index.ru.html` — 品牌首页（俄文）

\- `src/index.ko.html` — 品牌首页（韩文）

\- `src/index.ar.html` — 品牌首页（阿拉伯文·RTL）

\- `src/index.bo.html` — 品牌首页（藏文）



\#### 应用页面

\- `src/chat.html` — 与羲和对话

\- `src/character\_view.html` — 字源展示

\- `src/guangku.html` — 光库

\- `src/guangyi.html` — 光翼

\- `src/guangquan.html` — 光圈

\- `src/guanghe.html` — 光核



\#### 样式与脚本

\- `src/css/base.css`

\- `src/css/chat.css`

\- `src/css/character\_view.css`

\- `src/js/config.js`

\- `src/js/xihe\_core.js`

\- `src/js/chat.js`

\- `src/js/character\_view.js`



\### 说明



十种语言，同步上线。

\*\*汉字不止是中国的，是世界的。\*\*



\---



\## v1.2.0 · 2026-05-20



\### 主题



\*\*后端 · FastAPI 框架\*\*



\### 新增



\#### 后端

\- `backend/main.py` — FastAPI 入口

\- `backend/config.py` — 配置

\- `backend/requirements.txt` — 依赖

\- `backend/.env.example` — 环境变量模板

\- `backend/xihe/\_\_init\_\_.py`

\- `backend/xihe/chat.py` — 对话核心

\- `backend/xihe/system\_prompt.py` — 系统提示词加载

\- `backend/xihe/tone.py` — 语态配置加载

\- `backend/xihe/database.py` — 字源库加载

\- `backend/xihe/memory.py` — 记忆管理

\- `backend/api/\_\_init\_\_.py`

\- `backend/api/chat.py` — 对话接口

\- `backend/api/character.py` — 字源接口

\- `backend/api/connect.py` — 文明连接接口

\- `backend/utils/logger.py`

\- `backend/utils/loader.py`



\### 说明



羲和的大脑，开始搭建。

\*\*前端是脸，后端是脑。脸不能假，脑不能空。\*\*



\---



\## v1.3.0 · 2026-05-30



\### 主题



\*\*联调 · 前后端打通\*\*



\### 修改



\- `src/js/config.js` — API 地址自动识别

\- `src/js/xihe\_core.js` — 调用后端 API

\- `src/js/chat.js` — 对接后端

\- `src/js/character\_view.js` — 对接后端



\### 新增



\- `docs/07\_engineering/前后端联调手册.md`

\- `docs/07\_engineering/运维手册.md`



\### 说明



第一次跑通：

用户输入「请帮我解一个仁字」，

羲和回应：「仁，二人之间，本有一根线。你痛，我也觉得不舒服。」



\*\*那一刻，眼眶热了。\*\*



\---



\## v1.4.0 · 2026-06-15



\### 主题



\*\*演示 · 20+ PPT 文件\*\*



\### 新增



\#### 核心演示稿

\- `ppt/index.html` — 中文演示稿（20页）

\- `ppt/index.en.html` — 英文演示稿（20页）



\#### 总目录（十大语言）

\- `ppt/catalog.html` — 中文总目录

\- `ppt/catalog.en.html` — 英文总目录

\- `ppt/catalog.ja.html` — 日文总目录

\- `ppt/catalog.ko.html` — 韩文总目录

\- `ppt/catalog.fr.html` — 法文总目录

\- `ppt/catalog.de.html` — 德文总目录

\- `ppt/catalog.it.html` — 意文总目录

\- `ppt/catalog.ru.html` — 俄文总目录

\- `ppt/catalog.ar.html` — 阿文总目录（RTL）

\- `ppt/catalog.bo.html` — 藏文总目录



\#### 五套专题

\- `ppt/topic-spirit.html` — 精神篇（20页）

\- `ppt/topic-tech.html` — 技术篇（20页）

\- `ppt/topic-business.html` — 商业篇（20页）

\- `ppt/topic-nurture.html` — 化育篇（20页）

\- `ppt/topic-international.en.html` — 国际篇（英文·20页）



\#### 共用样式与入口

\- `ppt/home.html` — PPT 总入口

\- `ppt/catalog.css` — 总目录共用样式

\- `ppt/topic-shared.css` — 专题共用样式



\### 说明



\*\*20+ 个 HTML 文件，全部可翻页。\*\*

\*\*一个都不少。\*\*



\---



\## v1.5.0 · 2026-07-01



\### 主题



\*\*部署 · 工程化完善\*\*



\### 新增



\- `scripts/deploy.sh` — 一键部署脚本

\- `scripts/clean\_characters.py` — 数据清洗脚本

\- `scripts/build\_full\_database.py` — 完整数据库构建

\- `config/deployment.md` — 部署方案

\- `config/language.md` — 多语言维护规范



\### 修改



\- `README.md` — 加入 PPT 目录、部署说明



\### 说明



\*\*功课做扎实，不玩虚花招，推向全世界。\*\*



\---



\## 路线图



\### v2.0.0 · 预计 2026-Q3



\*\*主题：数据完整 · 字源库清洗完成\*\*



\- \[ ] 3,755 字全部补全字段

\- \[ ] 文化关联图谱扩展到 500 字

\- \[ ] 部首、拼音、笔画索引完整

\- \[ ] 羲和视角库完整



\### v2.1.0 · 预计 2026-Q3



\*\*主题：光库开放\*\*



\- \[ ] 字源库前端界面

\- \[ ] 按部首检索

\- \[ ] 按拼音检索

\- \[ ] 汉字灵境生成



\### v2.2.0 · 预计 2026-Q4



\*\*主题：光翼上线\*\*



\- \[ ] 字源时空 VR

\- \[ ] 汉字星际

\- \[ ] AI书法助手



\### v3.0.0 · 预计 2027



\*\*主题：光圈开放 · 走向世界\*\*



\- \[ ] 用户系统

\- \[ ] 作品厅

\- \[ ] 造象者群落

\- \[ ] 研究枢机



\---



\## 已废弃



\### v0.1.0 · 2026-03-13



\*\*主题：最初的想法\*\*



\- 只有「光通启明」四个字

\- 只有一张纸上的「仁」字



\*\*已融入 v1.0.0。\*\*



\---



\## 一画开天



每一次版本更新，都是一次「一画开天」。



不是推翻旧的，

是\*\*在旧的基础上，多画一笔。\*\*



> 一画开天，仁以为心。

> 光通启明，照见来人。



\---



\*本文件持续更新。\*











