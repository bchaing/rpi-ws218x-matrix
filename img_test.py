import PIL.Image
import numpy as np

image = PIL.Image.open("./sample.png")

image = image.resize((16,16))
image = np.asarray(image)
