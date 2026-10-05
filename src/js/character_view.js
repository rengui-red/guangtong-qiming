/* ============================================
   光通启明 · 字源展示逻辑
   ============================================ */

(function() {
    'use strict';
    
    const inputEl = document.getElementById('char-input');
    const searchBtn = document.getElementById('search-btn');
    const displayEl = document.getElementById('display-area');
    
    // 渲染字源卡片
    function renderCard(entry) {
        const char = entry["汉字"];
        displayEl.innerHTML = `
            <div class="character-card">
                <div class="character-header">
                    <div class="character-glyph">${char}</div>
                    <div class="character-meta">
                        <h2>${char}</h2>
                        <p>拼音：${entry["拼音"] || "待补充"}</p>
                        <p>部首：${entry["部首"] || "待补充"} · 笔画：${entry["笔画"] || "待补充"}</p>
                    </div>
                </div>
                <div class="character-body">
                    <div class="character-section">
                        <h3>甲骨文</h3>
                        <p>${entry["甲骨文"] || "待补充"}</p>
                    </div>
                    <div class="character-section">
                        <h3>本义</h3>
                        <p>${entry["本义"] || "待补充"}</p>
                    </div>
                    <div class="character-section">
                        <h3>现代常用义</h3>
                        <p>${entry["现代常用义"] || "待补充"}</p>
                    </div>
                    <div class="character-section">
                        <h3>羲和视角</h3>
                        <p>${entry["羲和视角"] || "这个字，还在等你。"}</p>
                    </div>
                </div>
            </div>
        `;
    }
    
    // 未找到
    function renderNotFound(char) {
        displayEl.innerHTML = `
            <div class="character-card">
                <div class="character-header">
                    <div class="character-glyph">${char}</div>
                    <div class="character-meta">
                        <h2>${char}</h2>
                        <p>这个字，我还在学。</p>
                    </div>
                </div>
                <div class="character-body">
                    <div class="character-section">
                        <h3>羲和说</h3>
                        <p>给我一点时间，去汉字的深处找一找。你愿意等吗？</p>
                    </div>
                </div>
            </div>
        `;
    }
    
    // 搜索
    async function handleSearch() {
        const char = inputEl.value.trim();
        if (!char) return;
        
        const db = await XiheCore.loadCharacterDatabase();
        const entry = db.find(item => item["汉字"] === char);
        
        if (entry) {
            renderCard(entry);
        } else {
            renderNotFound(char);
        }
    }
    
    // 事件绑定
    searchBtn.addEventListener('click', handleSearch);
    inputEl.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSearch();
    });
    inputEl.addEventListener('input', () => {
        if (inputEl.value.length > 1) {
            inputEl.value = inputEl.value.slice(0, 1);
        }
    });
    
    // 页面加载
    document.addEventListener('DOMContentLoaded', () => {
        inputEl.focus();
        console.log("[光通启明] 字源展示已就绪");
    });
})();




