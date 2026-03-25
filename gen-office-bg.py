#!/usr/bin/env python3
"""Generate a pixel-art office background with 7 distinct desk areas"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1280, 720
img = Image.new('RGB', (W, H), '#1a1a2e')  # 深色科技感底色
draw = ImageDraw.Draw(img)

# 地板 - 深灰格子
for y in range(0, H, 40):
    for x in range(0, W, 40):
        c = '#252540' if (x // 40 + y // 40) % 2 == 0 else '#1e1e38'
        draw.rectangle([x, y, x+39, y+39], fill=c)

# 墙壁（顶部）
draw.rectangle([0, 0, W, 100], fill='#2d2d4a')
# 墙壁底边装饰线
draw.rectangle([0, 98, W, 102], fill='#4a4a6a')

# 公司名牌匾 (居中顶部)
draw.rectangle([440, 20, 840, 80], fill='#3d2b1f', outline='#6b4226', width=3)
# 牌匾文字用简单方式

# 天花板灯 (3盏)
for lx in [320, 640, 960]:
    draw.rectangle([lx-30, 0, lx+30, 15], fill='#555580')
    draw.rectangle([lx-20, 15, lx+20, 25], fill='#aabbff', outline='#8899dd')
    # 灯光投射效果
    for i in range(5):
        alpha_rect = [lx-60-i*8, 25, lx+60+i*8, 35+i*5]
        c = f'#{"2a2a" + hex(0x50 - i*12)[2:].zfill(2)}'

# 7 个办公桌区域
# 上排 4 个 (y=200-320)
# 下排 3 个 (y=400-520)

DESKS = [
    # 上排
    {'x': 180, 'y': 250, 'name': 'Sky 🌤️'},
    {'x': 420, 'y': 250, 'name': 'K哥 📋'},
    {'x': 660, 'y': 250, 'name': 'Pin哥 📌'},
    {'x': 900, 'y': 250, 'name': 'Max 🔧'},
    # 下排
    {'x': 280, 'y': 460, 'name': '波哥 🌊'},
    {'x': 560, 'y': 460, 'name': 'Jr 🎨'},
    {'x': 840, 'y': 460, 'name': 'Yang 🧪'},
]

for d in DESKS:
    x, y = d['x'], d['y']
    
    # 桌子阴影
    draw.ellipse([x-55, y+25, x+55, y+45], fill='#0a0a18')
    
    # 办公桌 (深木色)
    draw.rectangle([x-50, y-5, x+50, y+25], fill='#5c3a1e', outline='#3e2510', width=2)
    # 桌面高光
    draw.rectangle([x-48, y-3, x+48, y+3], fill='#7a4e2e')
    
    # 显示器
    draw.rectangle([x-22, y-40, x+22, y-8], fill='#1a1a2e', outline='#444466', width=2)
    # 屏幕亮光 (青色 科技感)
    draw.rectangle([x-18, y-36, x+18, y-12], fill='#0a3a4a')
    # 屏幕扫描线效果
    for sy in range(y-36, y-12, 3):
        draw.line([x-18, sy, x+18, sy], fill='#0e4a5a', width=1)
    # 显示器支架
    draw.rectangle([x-3, y-8, x+3, y-2], fill='#444466')
    
    # 键盘
    draw.rectangle([x-15, y+5, x+15, y+12], fill='#333355', outline='#444477')
    
    # 鼠标
    draw.ellipse([x+20, y+6, x+28, y+13], fill='#333355', outline='#444477')
    
    # 椅子 (在桌子后面)
    draw.ellipse([x-18, y+30, x+18, y+55], fill='#2a2a4a', outline='#3a3a5a')
    draw.rectangle([x-15, y+28, x+15, y+35], fill='#2a2a4a')

# 右侧装饰 - 服务器机架
for ry in range(130, 600, 50):
    draw.rectangle([1120, ry, 1200, ry+40], fill='#1e2a3a', outline='#2a3a4a')
    # 指示灯
    draw.ellipse([1130, ry+15, 1136, ry+21], fill='#22cc55')
    draw.ellipse([1142, ry+15, 1148, ry+21], fill='#ffaa00')

# 左侧装饰 - 白板
draw.rectangle([20, 120, 120, 280], fill='#f0f0e8', outline='#888888', width=2)
# 白板上的线条
for ly in range(140, 270, 20):
    draw.line([30, ly, 110, ly], fill='#ccccbb', width=1)

# 底部状态栏区域
draw.rectangle([0, H-60, W, H], fill='#12122a')
draw.rectangle([0, H-62, W, H-60], fill='#4a4a6a')

# 保存
out = os.path.join(os.path.dirname(__file__), 'frontend', 'office_bg_small.png')
img.save(out, 'PNG')
print(f'Saved to {out} ({os.path.getsize(out)} bytes)')

# Also save as webp
out_webp = out.replace('.png', '.webp')
img.save(out_webp, 'WEBP', quality=90)
print(f'Saved to {out_webp} ({os.path.getsize(out_webp)} bytes)')
