from PIL import Image

def bilde():
    datne = "bilde.jpg"
    with Image.open(datne) as im:
        print(datne, im.format, f"{im.size}x{im.mode}")
        im.show()
        izmers = (100, 100)
        im.thumbnail(izmers)
        im.save("bilde-maza.jpg", im.format)
        im.show()

bilde()