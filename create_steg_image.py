from PIL import Image, ImageDraw, ImageFont
import os

# Create directory if not exists
os.makedirs('static/images', exist_ok=True)

# Create a basic image
img = Image.new('RGB', (400, 200), color = (0, 0, 0))
d = ImageDraw.Draw(img)
d.text((50, 90), "TOP SECRET // CLASSIFIED", fill=(0, 255, 65))

# Save it
img_path = 'static/images/level2_challenge.png'
img.save(img_path)

# Append the secret key to the file (Simple Steganography)
with open(img_path, 'ab') as f:
    f.write(b'\n\n-- SECRET DATA --\nKEY: GHOST_PROTOCOL\n-- END DATA --')

print(f"Created {img_path} with hidden message.")
