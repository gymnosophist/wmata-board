from wmata.config import STATION_CODE, WMATA_API_KEY 
from wmata.trains import get_trains
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics 
import os 
import time 

BASE_DIR=os.path.expanduser('~/Projects/wmata-led-board')
FONT_PATH=os.path.join(BASE_DIR, 'lib/rgbmatrix/fonts/4x6.bdf')

trains = get_trains()




# matrix configuration 
def setup_matrix(rows=32, cols=64, chain_length=1, parallel=1): 
    """
    Establishes matrix options. 
    Rows: Number of rows on the matrix.
    Cols: Number of columns. 
    Chain: Number of matrices in chain. 
    Parallel: Number of matrices in parallel. 
    """
    options = RGBMatrixOptions()
    options.rows=rows 
    options.cols=cols 
    options.chain_length = chain_length 
    options.parallel = parallel 
    options.hardware_mapping = 'adafruit-hat' #using the adafruit hat for this project; could set to 'regular' 
    options.gpio_slowdown = 4  # Working with Raspberry Pi 4
    options.brightness = 75

    return RGBMatrix(options = options)



def render_trains(trains: dict):
    """
    Renders a dictionary of trains 
    """
    matrix = setup_matrix()
    canvas = matrix.CreateFrameCanvas() 

    # define a dictionary of line colors 

    LINE_COLORS = {
    "SV": graphics.Color(192, 192, 192),  # Silver
    "BL": graphics.Color(0, 0, 255),      # Blue
    "OR": graphics.Color(255, 140, 0),    # Orange
    "YL": graphics.Color(255, 255, 0),    # Yellow
    "GR": graphics.Color(0, 255, 0),      # Green
    "RD": graphics.Color(255, 0, 0),      # Red
    }


    # load font 
    font = graphics.Font() 
    font.LoadFont(FONT_PATH)  # update path as needed
    textColor = graphics.Color(255, 0, 0)  # Yellow-ish text to start
    red = graphics.Color(255, 0, 0)
    yellow = graphics.Color(255, 255, 0)

    canvas.Clear() 

    # Render the HEADER 
    header_text = "LN     DEST     MIN"
    graphics.DrawText(canvas, font, 10, 7, header_text)
    
    # render train data 
    for i, train in enumerate(trains):
        # define y offset -- how much space there is between lines 
        y_offset = 8 + (i + 1) * 8 
        line = train["Line"]
        dest = (train["Destination"] or "").ljust(8)[:8]
        mins = (train["Min"] or "").rjust(3)

        # draw color block to indicate line 
        color = LINE_COLORS.get(line, graphics.Color(255,255,255)) # get color from dictionary unless not found, in which case return white 
        block_x = 2 
        block_y = 6
        for dx in range(block_x):
            for dy in range(block_y):
                canvas.SetPixel(dx, y_offset - block_y + dy, color.red, color.green, color.blue)
        # draw destination and minutes 
        graphics.DrawText(canvas, font, 10, y_offset, red, f"{dest[:8]} {mins}")
    # keep the image on screen 
    matrix.SwapOnVSync(canvas) 
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass




