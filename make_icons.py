from PIL import Image, ImageDraw
import os

os.makedirs('/home/claude/ig-saves/public', exist_ok=True)

for size in [192, 512]:
    img = Image.new('RGB', (size, size), '#E1306C')
    draw = ImageDraw.Draw(img)
    
    margin = size // 5
    bw = size - margin * 2
    bh = int(bw * 1.25)
    bx = margin
    by = (size - bh) // 2
    
    r = size // 10
    draw.rounded_rectangle([bx, by, bx+bw, by+bh], radius=r, fill='white')
    
    triangle_top = by + bh - size//8
    draw.polygon([
        (bx + bw//2, by + bh),
        (bx + bw//3, triangle_top),
        (bx + 2*bw//3, triangle_top)
    ], fill='#E1306C')
    
    dot_r = size // 20
    draw.ellipse([
        bx + bw//2 - dot_r,
        by + bh//2 - dot_r,
        bx + bw//2 + dot_r,
        by + bh//2 + dot_r
    ], fill='#E1306C')
    
    img.save(f'/home/claude/ig-saves/public/icon-{size}.png')
    print(f'Created icon-{size}.png')

print('Icons created!')
