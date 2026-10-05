\# 光通启明 · 多语言维护规范



> 上海易通和维科技有限责任公司

> yitonghewei.com



\---



\## 一、支持语言清单



| 代码 | 语言 | 文件名 | 状态 |

|------|------|--------|------|

| zh | 中文 | `index.html` | ✅ 默认 |

| en | English | `index.en.html` | ✅ |

| fr | Français | `index.fr.html` | ✅ |

| de | Deutsch | `index.de.html` | ✅ |

| it | Italiano | `index.it.html` | ✅ |

| ja | 日本語 | `index.ja.html` | ✅ |

| ru | Русский | `index.ru.html` | ✅ |

| ko | 한국어 | `index.ko.html` | ✅ |

| ar | العربية | `index.ar.html` | ✅ RTL |

| bo | བོད་ཡིག | `index.bo.html` | ⚠️ 待专家审校 |



\---



\## 二、文件命名规则



\### 规则



ndex.html ← 默认语言（中文）

index.\[语言代码].html ← 其他语言





\### 语言代码标准



采用 \*\*ISO 639-1\*\* 双字母代码：



\- 中文 → `zh`

\- 英文 → `en`

\- 法文 → `fr`

\- 德文 → `de`

\- 意大利文 → `it`

\- 日文 → `ja`

\- 俄文 → `ru`

\- 韩文 → `ko`

\- 阿拉伯文 → `ar`

\- 藏文 → `bo`



\---



\## 三、页面结构规范



\### 所有语言版本必须保持一致的结构



&#x20; 1，<head> - meta charset：UTF-8 - meta viewport：一致 - meta author：公司名（对应语言） - meta description：对应语言 - <title>：对应语言



&#x20; 2，<body> - 语言切换器（.lang-switcher） - 光点扩散动画（.splash） - 首屏（.hero） - logo-top - main-title-row（左标题 + 旦字图形 + 右标题） - sub-title（副标题） - tri-nav（导航：光库/光翼/光圈/问羲和） - scroll-hint - 光库（#guangku） - 光翼（#guangyi） - 光圈（#guangquan） - 光核（.core-area） - 页脚（.footer） - <script>（语言切换 + 平滑滚动）





\### 每种语言版本，结构完全相同，只替换文字



\---



\## 四、语言切换器规范



\### 每个页面的语言切换器位置



```html

<body>

&#x20;   <!-- 语言切换器必须放在 body 的第一个子元素 -->

&#x20;   <div class="lang-switcher">

&#x20;       <a href="index.html">中文</a>

&#x20;       <a href="index.en.html">EN</a>

&#x20;       <a href="index.fr.html">FR</a>

&#x20;       <a href="index.de.html">DE</a>

&#x20;       <a href="index.it.html">IT</a>

&#x20;       <a href="index.ja.html">JA</a>

&#x20;       <a href="index.ru.html">RU</a>

&#x20;       <a href="index.ko.html">KO</a>

&#x20;       <a href="index.ar.html">AR</a>

&#x20;       <a href="index.bo.html">བོད</a>

&#x20;   </div>

&#x20;   ...

</body>







