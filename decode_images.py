import codecs
import base64

def decodeImg(fileName):
    file = open(fileName, "r")
    currentLine = 0
    imgHex = ""
    for line in file:
        if currentLine > 1:
            imgHex += line[line.index("RECV,")+5:]
        currentLine += 1
    imgHex = imgHex.replace("\n", "")
    imgHex = imgHex.replace("\r", "")
    b64 = codecs.encode(codecs.decode(imgHex, 'hex'), 'base64').decode()
    
    return b64

#print(decodeImg("image.txt"))

with open("image.png", "wb") as fh:
    fh.write(str.encode(decodeImg("image.txt")))