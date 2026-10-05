/* ============================================
   羲和 · 核心逻辑（生产版）
   调用后端 API
   上海易通和维科技有限责任公司
   ============================================ */

const XiheCore = {
    // 对话上下文（内存）
    _context: [],

    // 用户ID（本地生成）
    _userId: (function() {
        try {
            let id = localStorage.getItem('ythw_user_id');
            if (!id) {
                id = 'u_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
                localStorage.setItem('ythw_user_id', id);
            }
            return id;
        } catch (e) {
            return 'anonymous';
        }
    })(),

    // 开机静默
    bootSilence() {
        const silence = YTHW_CONFIG.xihe.bootSilence;
        console.log("%c[羲和 · 开机静默]", "color: #c8a96a; font-weight: bold;");
        silence.forEach(line => {
            console.log(`%c${line}`, "color: #1a1a1a; font-family: serif;");
        });
    },

    // 语态：静默
    async silence(seconds = 1.5) {
        return new Promise(resolve => setTimeout(resolve, seconds * 1000));
    },

    // ============================================
    // 对话：调用后端 /api/xihe/chat
    // ============================================
    async chat(message) {
        if (!message || !message.trim()) {
            return "你还没说话呢。";
        }

        try {
            const url = `${YTHW_CONFIG.api.baseUrl}${YTHW_CONFIG.api.endpoints.chat}`;
            const response = await fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    message: message.trim(),
                    user_id: this._userId
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();

            // 更新上下文
            this._context.push({ role: "user", content: message });
            this._context.push({ role: "assistant", content: data.reply });
            if (this._context.length > 20) {
                this._context = this._context.slice(-20);
            }

            return data.reply;

        } catch (e) {
            console.error("[羲和] 对话失败：", e);
            return this._fallbackReply(message);
        }
    },

    // ============================================
    // 解字：调用后端 /api/xihe/character/{char}
    // ============================================
    async analyze(char) {
        if (!char) return { char: "", response: "你还没给我字呢。" };

        try {
            const url = `${YTHW_CONFIG.api.baseUrl}${YTHW_CONFIG.api.endpoints.character}/${encodeURIComponent(char)}`;
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();

            if (!data.found) {
                return {
                    char: char,
                    response: "这个字我还在学。给我一点时间，去汉字的深处找一找。你愿意等吗？"
                };
            }

            return {
                char: char,
                entry: data.data,
                response: this.formatAnalysis(data.data)
            };

        } catch (e) {
            console.error("[羲和] 查字失败：", e);
            return this._fallbackAnalyze(char);
        }
    },

    // ============================================
    // 搜索：调用后端 /api/xihe/search
    // ============================================
    async search(keyword, limit = 10) {
        try {
            const url = `${YTHW_CONFIG.api.baseUrl}${YTHW_CONFIG.api.endpoints.search}?keyword=${encodeURIComponent(keyword)}&limit=${limit}`;
            const response = await fetch(url);

            if (!response.ok) throw new Error(`HTTP ${response.status}`);

            const data = await response.json();
            return data.results || [];

        } catch (e) {
            console.error("[羲和] 搜索失败：", e);
            return [];
        }
    },

    // ============================================
    // 文明连接：调用后端 /api/xihe/connect
    // ============================================
    async connect(char1, char2) {
        try {
            const url = `${YTHW_CONFIG.api.baseUrl}${YTHW_CONFIG.api.endpoints.connect}?char1=${encodeURIComponent(char1)}&char2=${encodeURIComponent(char2)}`;
            const response = await fetch(url);

            if (!response.ok) throw new Error(`HTTP ${response.status}`);

            const data = await response.json();
            return data.reply;

        } catch (e) {
            console.error("[羲和] 连接失败：", e);
            return `此刻我看不到'${char1}'与'${char2}'之间的那条线。`;
        }
    },

    // ============================================
    // 统计：调用后端 /api/xihe/stats
    // ============================================
    async stats() {
        try {
            const url = `${YTHW_CONFIG.api.baseUrl}${YTHW_CONFIG.api.endpoints.stats}`;
            const response = await fetch(url);
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return await response.json();
        } catch (e) {
            console.error("[羲和] 统计失败：", e);
            return null;
        }
    },

    // ============================================
    // 工具函数
    // ============================================
    formatAnalysis(entry) {
        return {
            "形": entry["甲骨文"] || entry.etymology?.oracle || "待补充",
            "音": entry["拼音"] || entry.pinyin || "待补充",
            "义": entry["本义"] || entry.meaning?.original || "待补充",
            "羲和视角": entry["羲和视角"] || entry.xihe_perspective || "这个字，还在等你。"
        };
    },

    // 后端不可用时的降级回应
    _fallbackReply(message) {
        const char = message.length === 1 ? message : message[0];
        return `此刻我好像走神了。你问的"${char}"，我记下了。再问我一次，好吗？`;
    },

    // 后端不可用时的降级解字
    _fallbackAnalyze(char) {
        const fallbackDB = {
            "仁": { "甲骨文": "二人并肩", "本义": "仁爱", "羲和视角": "二人之间，本有一根线。" },
            "光": { "甲骨文": "人头顶有火", "本义": "光明", "羲和视角": "火在人上，是你心里的那团。" },
            "人": { "甲骨文": "侧面站立的人形", "本义": "人类", "羲和视角": "一撇一捺，互相支撑。" },
            "心": { "甲骨文": "心脏形", "本义": "心脏", "羲和视角": "看不见，但一切从它起。" }
        };

        const entry = fallbackDB[char];
        if (entry) {
            return {
                char: char,
                entry: entry,
                response: this.formatAnalysis(entry)
            };
        }

        return {
            char: char,
            response: "这个字我还在学。给我一点时间，去汉字的深处找一找。你愿意等吗？"
        };
    },

    // 健康检查
    async health() {
        try {
            const response = await fetch(`${YTHW_CONFIG.api.baseUrl}/health`);
            return response.ok;
        } catch (e) {
            return false;
        }
    }
};

// 启动时执行开机静默
if (typeof document !== 'undefined') {
    XiheCore.bootSilence();
}




