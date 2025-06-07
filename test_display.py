# written by chatgpt

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

# Matrix configuration
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # Or 'regular' if not using the Adafruit HAT

matrix = RGBMatrix(options=options)

# Create a new image to draw on
image = Image.new("RGB", (64, 32))
draw = ImageDraw.Draw(image)

# Load a default or custom font
font = ImageFont.load_default()
# Optional: use a .bdf font like the demo font:
# font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)

# Draw text
draw.text((2, 10), "Hello Metro!", fill=(255, 255, 0), font=font)

# Display it
matrix.SetImage(image)
