/* ============================================
   羲和 · 核心逻辑（极简防弹版）
   ============================================ */
const XiheCore = {
    bootSilence() {
        console.log("[羲和 · 开机静默] 一画开天，仁以为心。");
    },
    async silence(seconds = 1.5) {
        return new Promise(resolve => setTimeout(resolve, seconds * 1000));
    },
    async chat(message) {
        if (!message || !message.trim()) return "你还没说话呢。";
        try {
            const url = YTHW_CONFIG.api.baseUrl + YTHW_CONFIG.api.endpoints.chat;
            const response = await fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: message, user_id: "test001" })
            });
            if (!response.ok) throw new Error("HTTP " + response.status);
            const data = await response.json();
            return data.reply;
        } catch (e) {
            console.error("[羲和] 对话失败：", e);
            return "此刻我好像走神了。你再问一次，好吗？";
        }
    },
    async analyze(char) {
        try {
            const url = YTHW_CONFIG.api.baseUrl + YTHW_CONFIG.api.endpoints.character + "/" + encodeURIComponent(char);
            const response = await fetch(url);
            if (!response.ok) throw new Error("HTTP " + response.status);
            const data = await response.json();
            return { char: char, entry: data, response: "【" + char + "】" + (data.pinyin || "") };
        } catch (e) {
            return { char: char, response: "这个字我还在学。" };
        }
    }
};
XiheCore.bootSilence();



