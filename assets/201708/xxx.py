import PIL.Image
from exceptions import IOError

img = PIL.Image.open("preview2.jpg")
destination = "preview3.jpg"
try:
    img.save(destination, "JPEG", quality=80, optimize=True, progressive=True)
except IOError:
    PIL.ImageFile.MAXBLOCK = img.size[0] * img.size[1]
    img.save(destination, "JPEG", quality=80, optimize=True, progressive=True)

