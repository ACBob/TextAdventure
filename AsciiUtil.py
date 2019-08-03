from PIL import Image
import math
import numpy as np

pallette = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def getAverageL(image,TrueColor=False):

    im = np.array(image)

    w,h = im.shape

    return np.average(im.reshape(w*h))

def openImageAsASCII(file,TrueColor):
    #Based Partly On https://www.geeksforgeeks.org/converting-image-ascii-image-python/
    if not type(file) == str:
        return Exception("Requires String Path!")
    try: image = Image.open(file)
    except FileNotFoundError: print('File not found!') ; return []
    usedImage = image.convert('L')
    #image.show()

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

            gsval = pallette[int((avg*69)/255)]

            #print(gsval)
            #r='255'
            #g='128'
            #b='1'
            
            r,g,b = rgb.getpixel((0,0))
            r,g,b = int(r),int(g),int(b)
            #print(r,g,b)
            if not TrueColor:
                #NOT TRUE COLOR.
                #Christ is this a mess, fix this at some point.
                #White becomes orange for some reason!
                if r > g and b:
                    color='31;1' #Red
                elif g > r and b:
                    color='32;1' #Green
                elif b > r and g:
                    color='34;1' #Blue


                #Mixes
                elif r == b and r>=113 and r <255 and g<199:
                    color='35' #Magenta
                elif r == g and r>=127 and r<255 and g>=199 and g<255:
                    color='33' #Orange
                elif g == b and g>=233 and r <255:
                    color='36' #Cyan
                
                

                #GrayScales.
                elif r == b == g and r < 204 and r >128:
                    color='37' #Gray
                elif r == b == g and r >=204:
                    color='37;1' #White
                elif r == b == g and r<=128 and r>1:
                    color='30;1' #Dark Gray
                elif r == b == g and r <=1:
                    color='30' #Black
                else:
                    #print('color for column %s failed!'%(i))
                    #print(r)
                    #print(g)
                    #print(b)
                    color='00'
            else:
                color=str(r)+';'+str(g)+';'+str(b)
            
            amig[j] += '\033['+'38;2;'+color+'m'+gsval+'\033[0m'
    
            #print(amig[j])

    #for i in amig:
    #    print(i.replace('\n',''))
    return amig

if __name__ == "__main__":
    Running = True
    global truecolor
    truecolor = None
    while truecolor == None:
        truecolor = input('True Color? ')
    if truecolor == 'y':
        truecolor = True
    else:
        truecolor = False
    while Running:
        i = input('Image: ')
        if i == 'stop':
            Running = False
        else:
            for j in openImageAsASCII(i,truecolor):
                print(j.replace('\n',''))
