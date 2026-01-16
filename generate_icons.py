import os
from PIL import Image, ImageDraw

def create_icon(size, filename):
    # Theme Colors
    # Foreground: Deep technical grey
    color = "#2C2C2C" 
    
    # Create transparent canvas
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw the "Epoch" Node (Minimalist Circle)
    padding = size * 0.1
    shape = [padding, padding, size - padding, size - padding]
    stroke_width = max(1, int(size * 0.08))
    
    draw.ellipse(shape, outline=color, width=stroke_width)
    
    # Draw Center Focus Dot
    center_radius = size * 0.15
    center = [
        (size/2) - center_radius, (size/2) - center_radius,
        (size/2) + center_radius, (size/2) + center_radius
    ]
    draw.ellipse(center, fill=color)

    # Output
    if not os.path.exists('icons'):
        os.makedirs('icons')
    
    img.save(f'icons/{filename}', 'PNG')
    print(f"Generated {filename}")

if __name__ == "__main__":
    create_icon(48, "icon-48.png")
    create_icon(96, "icon-96.png")