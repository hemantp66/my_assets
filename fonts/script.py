import os
from PIL import Image, ImageDraw, ImageFont

def generate_icon(font_path, image_size=(100, 100)):
    # Load the font and get its name
    font_name = os.path.basename(font_path).rsplit('.', 1)[0]
    font_name_draw = "Font"
    # Create a new image with a transparent background
    image = Image.new("RGBA", image_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    # Calculate the maximum font size that fits within the image bounds
    max_font_size = min(image_size) // 2
    font = None
    
    for size in range(max_font_size, 0, -1):
        try:
            font = ImageFont.truetype(font_path, size)
            text_bbox = draw.textbbox((0, 0), font_name_draw, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            if text_width <= image_size[0] and text_height <= image_size[1]:
                break
        except Exception as e:
            print(f"Error loading font {font_path}: {e}")
            return
    
    # Calculate position to center the text
    text_x = (image_size[0] - text_width) / 2
    text_y = (image_size[1] - text_height) / 2
    
    # Draw the text onto the image
    draw.text((text_x, text_y), font_name_draw, font=font, fill=(255, 255, 255, 255))
    
    # Save the image
    output_path = f"{font_name}.png"
    image.save(output_path)
    print(f"Icon saved to {output_path}")

# Read all font files in the current folder
for font_file in os.listdir('.'):
    if font_file.endswith(('.ttf', '.otf')):
        font_path = os.path.join('.', font_file)
        generate_icon(font_path, image_size=(400, 200))  # Customize size as needed