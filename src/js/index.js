/* ============================================
   光通启明 · 首页逻辑
   ============================================ */

(function() {
    'use strict';
    
    console.log(
        `%c${YTHW_CONFIG.project.name}`,
        "color: #c8a96a; font-size: 1.5rem; font-family: serif; font-weight: bold;"
    );
    console.log(
        `%c${YTHW_CONFIG.project.motto}`,
        "color: #1a1a1a; font-size: 1rem; font-family: serif;"
    );
    console.log(
        `%c© 2026 ${YTHW_CONFIG.company.name}`,
        "color: #999; font-size: 0.85rem;"
    );
    console.log(
        `%c${YTHW_CONFIG.company.domain}`,
        "color: #999; font-size: 0.85rem;"
    );
    
    // 页面加载完成后的欢迎
    document.addEventListener('DOMContentLoaded', () => {
        console.log("[光通启明] 首页已就绪");
    });
})();






