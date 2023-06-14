
import sys
from PIL import Image, ImageOps

shirt = Image.open("shirt.png")
input_image = Image.open(sys.argv[1])


resized_image = ImageOps.fit(input_image, shirt.size)

resized_image.paste(shirt, (0, 0), mask=shirt)

resized_image.save(sys.argv[2])