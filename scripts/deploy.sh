#!/bin/bash

# ============================================
# 光通启明 · 一键部署脚本
# 上海易通和维科技有限责任公司
# yitonghewei.com
# ============================================

set -e  # 遇错即停

# ============================================
# 配置区（请按实际情况修改）
# ============================================

# 服务器信息
SERVER_USER="root"
SERVER_HOST="your-server-ip-or-domain"
SERVER_PORT="22"
SERVER_PATH="/var/www/guangtong-qiming"

# 本地项目路径（脚本会自动识别）
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# 部署模式：all / ppt / src / docs / backend
DEPLOY_MODE="${1:-all}"

# ============================================
# 颜色输出
# ============================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
GOLD='\033[0;33m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }
log_gold() { echo -e "${GOLD}$1${NC}"; }

# ============================================
# 启动
# ============================================

log_gold "============================================"
log_gold "  光通启明 · 部署脚本"
log_gold "  上海易通和维科技有限责任公司"
log_gold "============================================"
echo ""

log_info "项目根目录：$PROJECT_ROOT"
log_info "部署模式：$DEPLOY_MODE"
log_info "目标服务器：$SERVER_USER@$SERVER_HOST:$SERVER_PATH"
echo ""

# ============================================
# 检查配置
# ============================================

if [ "$SERVER_HOST" = "your-server-ip-or-domain" ]; then
    log_error "请先修改脚本中的服务器配置（SERVER_HOST 等）"
    exit 1
fi

# ============================================
# 检查 SSH 连接
# ============================================

log_info "检查 SSH 连接..."

if ! ssh -p "$SERVER_PORT" -o ConnectTimeout=10 -o BatchMode=yes "$SERVER_USER@$SERVER_HOST" "echo ok" > /dev/null 2>&1; then
    log_warn "SSH 免密登录未配置，将需要输入密码。"
    log_warn "建议配置 SSH 密钥：ssh-copy-id -p $SERVER_PORT $SERVER_USER@$SERVER_HOST"
    echo ""
fi

# ============================================
# 确保目标目录存在
# ============================================

log_info "确保服务器目录存在..."
ssh -p "$SERVER_PORT" "$SERVER_USER@$SERVER_HOST" "mkdir -p $SERVER_PATH"
echo ""

# ============================================
# 按模式上传
# ============================================

deploy_all() {
    log_info "上传整个项目..."
    rsync -avz --delete \
        -e "ssh -p $SERVER_PORT" \
        --exclude='.git' \
        --exclude='node_modules' \
        --exclude='venv' \
        --exclude='__pycache__' \
        --exclude='.env' \
        --exclude='*.log' \
        --exclude='.DS_Store' \
        "$PROJECT_ROOT/" \
        "$SERVER_USER@$SERVER_HOST:$SERVER_PATH/"
}

deploy_ppt() {
    log_info "上传 PPT 演示稿..."
    rsync -avz --delete \
        -e "ssh -p $SERVER_PORT" \
        "$PROJECT_ROOT/ppt/" \
        "$SERVER_USER@$SERVER_HOST:$SERVER_PATH/ppt/"
}

deploy_src() {
    log_info "上传前端..."
    rsync -avz --delete \
        -e "ssh -p $SERVER_PORT" \
        "$PROJECT_ROOT/src/" \
        "$SERVER_USER@$SERVER_HOST:$SERVER_PATH/src/"
}

deploy_docs() {
    log_info "上传文档..."
    rsync -avz --delete \
        -e "ssh -p $SERVER_PORT" \
        "$PROJECT_ROOT/docs/" \
        "$SERVER_USER@$SERVER_HOST:$SERVER_PATH/docs/"
}

deploy_backend() {
    log_info "上传后端..."
    rsync -avz --delete \
        -e "ssh -p $SERVER_PORT" \
        --exclude='venv' \
        --exclude='__pycache__' \
        --exclude='.env' \
        "$PROJECT_ROOT/backend/" \
        "$SERVER_USER@$SERVER_HOST:$SERVER_PATH/backend/"
}

case "$DEPLOY_MODE" in
    all)
        deploy_all
        ;;
    ppt)
        deploy_ppt
        ;;
    src)
        deploy_src
        ;;
    docs)
        deploy_docs
        ;;
    backend)
        deploy_backend
        ;;
    *)
        log_error "未知部署模式：$DEPLOY_MODE"
        echo ""
        echo "用法：./deploy.sh [all|ppt|src|docs|backend]"
        exit 1
        ;;
esac

echo ""
log_info "上传完成。"

# ============================================
# 设置权限
# ============================================

log_info "设置服务器权限..."
ssh -p "$SERVER_PORT" "$SERVER_USER@$SERVER_HOST" "
    chmod -R 755 $SERVER_PATH
    chown -R www-data:www-data $SERVER_PATH 2>/dev/null || chown -R nginx:nginx $SERVER_PATH 2>/dev/null || true
"
echo ""

# ============================================
# 重载 Nginx（可选）
# ============================================

log_info "尝试重载 Nginx..."
ssh -p "$SERVER_PORT" "$SERVER_USER@$SERVER_HOST" "
    if command -v systemctl > /dev/null; then
        sudo systemctl reload nginx 2>/dev/null && echo 'Nginx 已重载' || echo '未重载 Nginx（可能未安装或权限不足）'
    fi
"
echo ""

# ============================================
# 完成
# ============================================

log_gold "============================================"
log_gold "  部署完成！"
log_gold "============================================"
echo ""
log_info "访问地址："
echo "  https://yitonghewei.com/ppt/"
echo "  https://yitonghewei.com/ppt/home.html"
echo ""
log_info "如遇问题，检查："
echo "  1. 服务器 Nginx 配置"
echo "  2. 文件权限"
echo "  3. 防火墙端口"
echo ""

log_gold "一画开天，仁以为心。"
log_gold "光通启明，照见来人。"



