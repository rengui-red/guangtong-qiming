/* ============================================
   光通启明 · 对话逻辑（防弹版）
   ============================================ */
(function() {
    'use strict';
    const messagesEl = document.getElementById('chat-messages');
    const inputEl = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const statusEl = document.getElementById('xihe-status');

    function addMessage(role, content) {
        const msg = document.createElement('div');
        msg.className = `message ${role}`;
        msg.innerHTML = `<div class="message-content">${content}</div>`;
        messagesEl.appendChild(msg);
        messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    async function handleSend() {
        const text = inputEl.value.trim();
        if (!text) return;
        addMessage('user', `<p>${text}</p>`);
        inputEl.value = '';
        if (statusEl) statusEl.textContent = "正在看……";
        
        const reply = await XiheCore.chat(text);
        addMessage('xihe', `<p>${reply}</p>`);
        if (statusEl) statusEl.textContent = "我在。";
    }

    sendBtn.addEventListener('click', handleSend);
    inputEl.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
    });
})();



