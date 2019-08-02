from PIL import Image
import math
import numpy as np

pallette = " .:-=+*#%@"

def getAverageL(image):

    im = np.array(image)

    w,h = im.shape

    return np.average(im.reshape(w*h))

def openImageAsASCII(file):
    if not type(file) == str:
        return Exception("Requires String Path!")
    image = Image.open(file)
    usedImage = image.convert('L')
    image.show()

    W,H = usedImage.size[0],usedImage.size[1]
    print(W)
    print(H)

    cols = 80
    scale = 0.43

    w = W/cols

    h = w/scale
    print(w)
    print(h)


    rows = int(H/h)
    global amig
    amig = []

    print(rows)

    for j in range(rows):
        y1=int(j*h)
        y2=int((j+1)*h)

        if j == rows-1:
            y2 = H

        amig.append("\n")


        for i in range(cols):
            x1 = int(i*w)
            x2 = int((i+1)*w)
            print(i)
            #print(x1)
            #print(x2)

            #print(i)
            
            img = usedImage.crop((x1,y1,x2,y2))
            #if j and i == 0: img.show()

            avg = int(getAverageL(img))

            gsval = pallette[int((avg*9)/255)]

            #print(gsval)

            amig[j] += gsval

    return amig
