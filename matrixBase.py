import board
import neopixel

# constants
pixelsX = 16
pixelsY = 16
numPixels = pixelsX * pixelsY

# initialize pixels
pixels = neopixel.NeoPixel(board.D18, numPixels,  auto_write=False)
matrix = []

# pixel element object
class Pixel:
        def __init__(self, i):
                self.index = i

	# set pixel's value without displaying
        def value(self,r,g,b):
                pixels[self.index] = (r,g,b)

	# set pixel's value and displays it
        def set(self,r,g,b,flush=False):
                if flush:
                        off()
                pixels[self.index] = (r,g,b)
                pixels.show()

	# turns off the pixel
        def reset(self):
                pixels[self.index] = (0,0,0)

# transform pixels to matrix
for x in range(pixelsX):
        row = []
        if x % 2 == 0:
                for y in range(pixelsY):
                        row.append(Pixel(y + pixelsY * x))
        else:
                for y in range(pixelsY):
                        row.append(Pixel((pixelsY * x + pixelsY - 1) - y))
        matrix.insert(x, row)

# helper functions
def reset():
        pixels.fill((0,0,0))
        pixels.show()
