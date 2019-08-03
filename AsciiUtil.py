from PIL import Image
import math
import numpy as np

pallette = "@%#*+=-:. "

def getAverageL(image,TrueColor=False):

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
    #print(W)
    #print(H)

    cols = 80
    scale = 0.43

    w = W/cols

    h = w/scale
    #print(w)
    #print(h)


    rows = int(H/h)
    global amig
    amig = []

    #print(rows)
    #SmolImage = image
    #SmolImage.thumbnail((int(w),int(h)), Image.NEAREST)
    
    #SmolImage = SmolImage.load()

    for j in range(rows):
        y1=int(j*h)
        y2=int((j+1)*h)

        if j == rows-1:
            y2 = H

        amig.append("\n")


        for i in range(cols):
            x1 = int(i*w)
            x2 = int((i+1)*w)
            #print(i)
            #print(x1)
            #print(x2)

            #print(i)
            
            img = usedImage.crop((x1,y1,x2,y2))
            imgColor = image.crop((x1,y1,x2,y2))
            rgb=imgColor.convert('RGB')
            #print(imgColor[0,0])
            #if j and i == 0: img.show()
            

            avg = int(getAverageL(img))

            gsval = pallette[int((avg*9)/255)]

            #print(gsval)
            #r='255'
            #g='128'
            #b='1'
            
            r,g,b = rgb.getpixel((0,0))
            r,g,b = int(r),int(g),int(b)
            #print(r,g,b)
            if not TrueColor:
                #NOT TRUE COLOR.
                if r > g and b:
                    color='101' #Red
                elif g > r and b:
                    color='102' #Green
                elif b > r and g:
                    color='104' #Blue
                #Mixes
                elif r == b and r and b > g:
                    color='45' #Magenta
                elif r == g and r and g > b:
                    color='43' #Orange
                elif g == b and r and g > r:
                    color='46' #Cyan
                

                #GrayScales.
                elif r == b == g and r < 204 and r >128:
                    color='47' #Gray
                elif r == b == g and r >=204:
                    color='107' #White
                elif r == b == g and r<=128 and r>1:
                    color='100' #Dark Gray
                elif r == b == g and r <=1:
                    color='40' #Black
                else:
                    #print('color for column %s failed!'%(i))
                    #print(r)
                    #print(g)
                    #print(b)
                    color='00'
            else:
                color=str(r)+';'+str(g)+';'+str(b)
            
            amig[j] += '\033['+'48;2;'+color+'m'+gsval+'\033[0m'
    
            #print(amig[j])

    #for i in amig:
    #    print(i.replace('\n',''))
    return amig
