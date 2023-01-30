from PIL import Image

def ppm2png(filename):
    im = Image.open(filename)
    filename, ext = filename.split(".")
    im.save(f"{filename}.png")