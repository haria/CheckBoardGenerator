import os, sys, time
from PIL import Image

if __name__=="__main__":
    checkpoint = 21
    blocksize = 177
    margin = 10
    
    if len(sys.argv) == 4:
        checkpoint = int(sys.argv[1])
        blocksize = int(sys.argv[2])
        margin = int(sys.argv[3])
    
    print("%s %d %d %d"%(sys.argv[0], checkpoint, blocksize, margin))
    
    img=Image.new('RGB',(blocksize*checkpoint+margin*2,blocksize*checkpoint+margin*2),(255,255,255))
    black=Image.new('RGB',(blocksize,blocksize),(0,0,0))

    for x in range(checkpoint):
        for y in range(checkpoint):
            if ((x%2==0) and  (y%2==0)) or ((x%2==1) and  (y%2==1)):
                img.paste( black, (blocksize*x+margin,y*blocksize+margin) )

    img.save("checkboard.jpg")
        