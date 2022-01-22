from time import sleep
import random
import board
import neopixel

import PIL.Image
import numpy as np

# constants
pixelsX = 16
pixelsY = 16
numPixels = pixelsX * pixelsY

pixels = neopixel.NeoPixel(board.D18, numPixels,  auto_write=False)
matrix = []

# pixel element object
class Pixel:
	def __init__(self, i):
		self.index = i

	def value(self,r,g,b):
		pixels[self.index] = (r,g,b)

	def set(self,r,g,b,flush=False):
		if flush:
			off()
		pixels[self.index] = (r,g,b)
		pixels.show()


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

# animations
def in_order_wipe(r,g,b,flush=True):
	for i in range(pixelsX):
		for j in range(pixelsY):
			matrix[i][j].value(r,g,b)
			pixels.show()
	if flush:
		reset()

def snake_wipe(r,g,b,flush=True):
	for i in range(numPixels):
		pixels[i] = (r,g,b)
		pixels.show()

	if flush:
		reset()

def graph(formula,trace=True,flush=True):
	for i in range(pixelsX):
		y = formula(i-pixelsX/2)
		#print(i,int(y+pixelsY//2))
		if y < pixelsY - pixelsY/2 and y >= -pixelsY/2:
			matrix[i][int(y+pixelsY/2)].value(255,255,255)
			pixels.show()
		if not trace:
			reset()
		sleep(.1)
	if flush:
		reset()

def display_image(image):
	image = PIL.Image.open("./sample.png")
	image = image.resize((16,16))
	image = np.asarray(image)

	#for x in range(pixelsX):
		#for y in range(pixelsY):

# run
try:
	while True:
		matrix[0][8].set(255,255,255)
except:
	reset()
	print("")

