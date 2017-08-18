import PIL.Image
import os

from exceptions import IOError

for name in os.listdir("."):
    if name.endswith(".png"):
        img = PIL.Image.open(name)
        img = img.convert("RGB")
        img.save(os.path.splitext(name)[0] + ".jpg", "JPEG", quality=80, optimize=True, progressive=True)


