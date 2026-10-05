\# 光通启明 · 部署方案



> 上海易通和维科技有限责任公司

> yitonghewei.com



\---



\## 一、部署目标



将“光通启明 · 汉字光宇世界”部署到 `yitonghewei.com`，

让全世界都能访问。



\---



\## 二、部署架构



用户浏览器

│

▼

yitonghewei.com

│

├── 静态页面（src/ 下的 HTML/CSS/JS）

│ ├── index.html

│ ├── guangku.html

│ ├── guangyi.html

│ ├── guangquan.html

│ ├── guanghe.html

│ ├── chat.html

│ └── character\_view.html

│

├── 静态资源（docs/ 下的 JSON 数据）

│ └── 05\_character\_database/\*.json

│

└── 后端API（未来接入）

└── api.yitonghewei.com





\---



\## 三、部署方案（三选一）



\### 方案A：GitHub Pages（最简单，免费）



\*\*适合：\*\* 现阶段，纯静态页面



\*\*步骤：\*\*



1\. 把整个项目推送到 GitHub

2\. 进入仓库 Settings → Pages

3\. Source 选择 `main` 分支，目录选 `/src`

4\. 保存，等待1分钟

5\. GitHub 自动分配地址：`https://\[用户名].github.io/guangtong-qiming/`

6\. 在 GitHub Pages 设置里，绑定自定义域名 `yitonghewei.com`



\*\*优点：\*\* 免费、稳定、自动部署

\*\*缺点：\*\* 无法运行后端API



\---



\### 方案B：国内服务器（推荐长期）



\*\*适合：\*\* 正式上线，需要后端支持



\*\*步骤：\*\*



1\. 购买服务器（阿里云/腾讯云，上海节点）

2\. 购买域名 `yitonghewei.com`，完成备案

3\. 配置服务器环境（Nginx）

4\. 把 `src/` 下的静态文件放到服务器 `/var/www/guangtong-qiming/`

5\. 配置 Nginx 指向这个目录

6\. 配置 SSL 证书（HTTPS）

7\. 配置域名解析指向服务器IP



\*\*Nginx 配置示例：\*\*



```nginx

server {

&#x20;   listen 80;

&#x20;   server\_name yitonghewei.com www.yitonghewei.com;

&#x20;   return 301 https://$server\_name$request\_uri;

}



server {

&#x20;   listen 443 ssl http2;

&#x20;   server\_name yitonghewei.com www.yitonghewei.com;



&#x20;   ssl\_certificate /etc/ssl/yitonghewei.com.crt;

&#x20;   ssl\_certificate\_key /etc/ssl/yitonghewei.com.key;



&#x20;   root /var/www/guangtong-qiming;

&#x20;   index index.html;



&#x20;   location / {

&#x20;       try\_files $uri $uri/ =404;

&#x20;   }



&#x20;   location /docs/ {

&#x20;       alias /var/www/guangtong-qiming/docs/;

&#x20;       add\_header Access-Control-Allow-Origin \*;

&#x20;   }



&#x20;   location /api/ {

&#x20;       proxy\_pass http://localhost:8000/;

&#x20;       proxy\_set\_header Host $host;

&#x20;       proxy\_set\_header X-Real-IP $remote\_addr;

&#x20;   }

}









