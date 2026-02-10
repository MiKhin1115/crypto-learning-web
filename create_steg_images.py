from PIL import Image, ImageDraw, ImageFont
import os

def create_steg_images():
    os.makedirs('static/images', exist_ok=True)
    
    challenges = [
        ("level2_1.png", "GHOST_PROTOCOL"),
        ("level2_2.png", "BLUE_SKY"),
        ("level2_3.png", "DEEP_DIVE"),
        ("level2_4.png", "DARK_WEB"),
        ("level2_5.png", "CYBER_PUNK")
    ]
    
    for filename, key in challenges:
        # Create a basic image
        img = Image.new('RGB', (400, 200), color = (0, 0, 0))
        d = ImageDraw.Draw(img)
        d.text((50, 90), f"CLASSIFIED // {filename}", fill=(0, 255, 65))
        
        path = f'static/images/{filename}'
        img.save(path)
        
        # Append secret
        with open(path, 'ab') as f:
            f.write(f'\n\n-- SECRET DATA --\nKEY: {key}\n-- END DATA --'.encode())
            
        print(f"Generated {path}")

if __name__ == "__main__":
    create_steg_images()
