import random
from PIL import Image, ImageDraw, ImageFont

def mm_to_px(mm, dpi=300):
    """Converts millimeters to pixels based on target DPI (300 for high quality print)."""
    return int((mm / 25.4) * dpi)

def generate_pixel_novel_cover(
    filename="novel_cover_60mm.png", 
    width_mm=60, 
    height_mm=90, 
    pixel_size=12, 
    dpi=300
):
    # Convert 60mm x 90mm dimensions to pixels
    width_px = mm_to_px(width_mm, dpi)
    height_px = mm_to_px(height_mm, dpi)

    # Multi-shade gray color palette
    gray_shades = [
        (30, 30, 36),    # Deep Charcoal
        (45, 49, 66),    # Dark Gray
        (79, 93, 117),   # Cool Slate Gray
        (141, 153, 174), # Medium Light Gray
        (191, 192, 192), # Silver Gray
        (108, 117, 125)  # Neutral Gray
    ]

    # 1. Create Base Image
    image = Image.new("RGB", (width_px, height_px))
    draw = ImageDraw.Draw(image)

    # 2. Draw Random Pixel Background
    for x in range(0, width_px, pixel_size):
        for y in range(0, height_px, pixel_size):
            color = random.choice(gray_shades)
            draw.rectangle(
                [x, y, x + pixel_size, y + pixel_size], 
                fill=color
            )

    # 3. Add Dark Overlays for Title/Author Text Boxes
    title_box_height = int(height_px * 0.18)
    
    # Header Box (Title)
    draw.rectangle([20, 20, width_px - 20, 20 + title_box_height], fill=(0, 0, 0, 200))
    draw.rectangle([20, 20, width_px - 20, 20 + title_box_height], outline=(191, 192, 192), width=3)

    # Footer Box (Author)
    footer_y = height_px - title_box_height - 20
    draw.rectangle([20, footer_y, width_px - 20, height_px - 20], fill=(0, 0, 0, 200))
    draw.rectangle([20, footer_y, width_px - 20, height_px - 20], outline=(191, 192, 192), width=3)

    # 4. Add Text
    try:
        title_font = ImageFont.truetype("arial.ttf", 36)
        sub_font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()

    # Draw Title
    draw.text((width_px // 2, 45), "NOVEL TITLE", fill=(255, 255, 255), font=title_font, anchor="mm")
    draw.text((width_px // 2, 85), "PIXEL EDITION", fill=(191, 192, 192), font=sub_font, anchor="mm")

    # Draw Author
    draw.text((width_px // 2, footer_y + (title_box_height // 2)), "BY AUTHOR NAME", fill=(255, 255, 255), font=sub_font, anchor="mm")

    # Save output
    image.save(filename, dpi=(dpi, dpi))
    print(f"Novel cover generated successfully: {filename} ({width_px}x{height_px}px at {dpi} DPI)")

if __name__ == "__main__":
    generate_pixel_novel_cover()
