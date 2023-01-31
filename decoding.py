import PIL
from PIL import Image

obr = Image.open("butterfly.png")
pixels = obr.load()

dlzka = 8

def decode():
    de = []
    for x in range(obr.size[0]):
        for y in range(obr.size[1]):
            pixelblue = pixels[x,y][2]
            blue = bin(pixelblue)
            de.append(blue[-1])
    return de

de = decode()
def decoding(de):
    sprava = ""
    cislo = ""
    for i in de:
        x = ""
        cislo += i
        if len(cislo) == dlzka:
            x = chr(int(cislo,2))
            sprava += x
            cislo = ""
        if "#" in sprava:
            break
    return sprava

print(decoding(de))