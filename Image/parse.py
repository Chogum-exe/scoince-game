from PIL import Image
import os

def imgcrop(input, xPieces, yPieces):
    filename, file_extension = os.path.splitext(input)
    im = Image.open(input)
    imgwidth, imgheight = im.size
    print(imgwidth, imgheight)
    height = imgheight // yPieces
    width = imgwidth // xPieces
    print(width, height)
    for i in range(0, xPieces):
        for j in range(0, yPieces):
            print('---------------------------------')
            print(i, j)
            box = (i * width, j * height, (i + 1) * width, (j + 1) * height)
            print(box)
            a = im.crop(box)
            try:
                a.save("../ScienceGame/Map/images/" + 'images' + str(i) + "-" + str(j) + file_extension)
            except:
                print('error')

imgcrop('image.png',10,10)
