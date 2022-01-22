from matrixBase import *
from time import sleep
import random

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
