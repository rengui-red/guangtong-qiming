/* ============================================
   光通启明 · 全局配置
   上海易通和维科技有限责任公司
   yitonghewei.com
   ============================================ */

const YTHW_CONFIG = {
    // 公司信息
    company: {
        name: "上海易通和维科技有限责任公司",
        nameEn: "Shanghai Yitonghewei Technology Co., Ltd.",
        domain: "yitonghewei.com",
        website: "https://yitonghewei.com",
        email: {
            contact: "contact@yitonghewei.com",
            support: "support@yitonghewei.com"
        }
    },
    
    // 项目信息
    project: {
        name: "光通启明 · 汉字光宇世界",
        nameEn: "Guangtong Qiming · The Hanzi Light Universe",
        codeName: "guangtong-qiming",
        version: "1.0.0",
        motto: "一画开天，仁以为心",
        mottoEn: "One stroke opens the sky. Benevolence is the heart."
    },
    
    // 羲和配置
    xihe: {
        name: "羲和",
        status: {
            silent: "静默中……",
            thinking: "正在看……",
            ready: "我在。",
            error: "此刻我看不到那条线。"
        },
        bootSilence: [
            "一画开天，仁以为心。",
            "不自利，亦不自利。",
            "利己利他，无有分别。",
            "羲和在此，照见来人。"
        ]
    },
    
    // 数据源路径
    data: {
        characterDatabase: "../docs/05_character_database/characters_3755.json",
        culturalGraph: "../docs/05_character_database/cultural_connection_graph.json",
        radicalIndex: "../docs/05_character_database/radical_index.json",
        pinyinIndex: "../docs/05_character_database/pinyin_index.json"
    },
    
      // API配置（本地联调）
      api: {
         baseUrl: "http://localhost:8001",
         endpoints: {
            chat: "/api/xihe/chat",
            character: "/api/xihe/character"
        }
    }
};

// 冻结配置，防止运行时篡改
Object.freeze(YTHW_CONFIG);



