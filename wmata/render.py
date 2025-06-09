from config import STATION_CODE, WMATA_API_KEY 
from trains import get_trains
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

    # load font 
    font = graphics.Font() 
    font.LoadFont(FONT_PATH)  # update path as needed
    textColor = graphics.Color(255, 255, 0)  # Yellow-ish text to start 

    y_offset = 10 # starting y position 

    canvas.Clear() 

    # render some train data 
    for train in trains[:3]: # limit to three trains for now 
        line = train['Line']
        car = train['Car']
        dest = train['Destination']
        mins = train['Min']
        # format the text 

        # text = f"{line:<2} {car:<1} {dest:<6} {mins:>2}" we'll leave the car argument out for now 
        text = f"{line} {dest[:7]} {car}".ljust(10) + f"{mins}".rjust(2)

        graphics.DrawText(canvas, font, 1, y_offset, textColor, text[:13])  # Clip to ~11 chars
        y_offset += 10

    matrix.SwapOnVSync(canvas)

    # keep the image on screen 
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass




