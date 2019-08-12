from tkinter import *
#import IMU
import time
import os
import math
from PIL import Image, ImageTk

def __init__(self):
    canvas=None
    self.triangle=None
    self.ziplineActual=None
    self.ziplineEstimate=None
    self.border=None
    self.border2=None
    self.root=None
    self.cube=None
    self.refresh=None
    self.w=None
    self.h=None
    self.x=None
    self.y=None

root=Tk()
w=1500
h=1000
x=0
y=0
root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.title("OTIS-2U")
frame=Frame(root, bg="white")
frame.pack(fill=BOTH, expand=1)
canvas = Canvas(root, bg="white", height=1000, width=1500)
triangle = canvas.create_line(100,80,100,290,282,185,100,80,fill="red", width=2)
ziplineEstimate = canvas.create_line(320, 85, 620, 85, fill= "red", width=2)
canvas.create_text(460, 110, font=('freemono bold',12),fill="blue", text="Estimated Zipline")
ziplineActual=canvas.create_line(320, 200, 620, 200, fill = "red", width=2)
canvas.create_text(460, 225, font=('freemono bold', 12), fill="blue", text="Actual Zipline")
border= canvas.create_line(300,30,300,350, fill="black", width=2)
border2=canvas.create_line(0,350,1100,350,fill="black", width=2)
border3=canvas.create_line(700,30,700,350, fil="black", width=2)
#dot = canvas.create_rectangle(97,83,103,77, fill="blue", width=2,)
#cube= canvas.create_rectangle(317,82, 323, 88, fill="blue", width=2)

canvas.create_text(65,180,font=('freemono bold',12), fill="blue", text="Leg AC")
canvas.create_text(200, 270,font=('freemono bold',12), fill="blue", text="Leg BC")
canvas.create_text(200, 100, font=('freemono bold',12), fill="blue", text= "Leg AB")
canvas.create_text(80, 50, font=('freemono bold', 12), fill="black",text="Woods Hole Zipline")
canvas.create_text(400, 50, font=('freemono bold',12), fill="black", text='Test Zipline')

#compass
canvas.create_line(800,175, 800, 230, fill="green", width=2)
canvas.create_line(800, 120, 800, 175, fill="green", width=2)
canvas.create_line(800,175,855,175, fill="green", width=2)
canvas.create_line(745, 175, 800, 175, fill="green", width=2)
canvas.create_line(772.5,147.5, 800, 175, fill="green", width=2)
canvas.create_line(800, 175,827.5, 202.5, fill="green", width=2)
canvas.create_line(800, 175,772.5, 202.5, fill="green", width=2)
canvas.create_line(800, 175, 827.5, 147.5, fill="orange", width=2)
canvas.create_text(800, 105, font=('freemono bold',12), fill ="blue", text="N")
canvas.create_text(800, 245, font=('freemono bold', 12), fill="blue", text="S")
canvas.create_text(865, 175, font=('freemono bold', 12), fill="blue", text='E')
canvas.create_text(730, 175, font=('freemono bold',12), fill="blue", text="W")

'''while True:
    if IMU.getDirection()=='N':
        canvas.create_line(800, 120, 800, 175, fill="orange", width=2)
    if IMU.getDirection()=='SE':
        canvas.create_line(800, 175,827.5, 202.5, fill="orange", width=2)
    if IMU.getDirection()=="SW":
        canvas.create_line(800, 175,772.5, 202.5, fill="orange", width=2)'''

#images
def refreshF():
    images={}
    imgnum=0
    pixeladdX=150
    coordX=100
    coordY=430
    path='C:\\Work\\BWSI\\CubeSats\\sat_images\\{}.jpg'
    while 1:
        for i in range(7):
            path_final=path.format(imgnum)
            if os.path.exists(path_final):
                img= Image.open(path_final)
                img=img.resize((128,128),Image.ANTIALIAS)
                pic=ImageTk.PhotoImage(img)
                pic.image=img    
                images[i]=pic
                new=canvas.create_image(coordX,coordY, image=pic)
                coordX+=pixeladdX
            print(os.path.exists(path_final))
            imgnum+=1
            root.update()
            root.after(100)
 
mydir= 'C:/Work/BWSI/CubeSats/sat_images/'
data=open(str(mydir) + "telemetry.txt", "r")
content=data.readlines()
pic0=content[1]
pic1=content[4]
pic2=content[7]
pic3=content[10]
pic4=content[13]
pic5=content[16]
pic6=content[19]
odomoterList=[pic0, pic1, pic2, pic3, pic4, pic5, pic6]
data.close()

#Actual Zipline Picture Location Calculation
factor=0
movt=0
dist=0
distance=0
i=0
for i in range(7):
    distance = odomoterList[i]
    factor = float(distance)/10.8
    movt=300*factor
    canvas.create_rectangle(317+movt, 197, 323+movt, 203, fill="blue", width=2)
    root.update()
    root.after(400)

canvas.pack()

def start():
    cube = canvas.create_rectangle(317,82, 323, 88, fill="blue", width=2)
    for i in range(150):
        canvas.move(cube, 2, 0)
        root.update()
        root.after(180)

#buttons
startEstimate=Button(frame, text="Start Estimate", bg="green", command=start)
refresh= Button(frame, text="Refresh", bg="green",command=refreshF)
refresh.pack()
startEstimate.pack()

#triangle zipline demo
def StartA():
    dot = canvas.create_rectangle(97,83,103,77, fill="blue", width=2,)
    while 1:
        #Leg AB
        for i in range(35):
            canvas.move(dot,5.25,3)
            root.update()
            root.after(1800)
        #Leg BC
        for i in range(35):
            canvas.move(dot,-5.25,3)
            root.update()
            root.after(1670)
        #Leg AC
        for i in range(70):
            canvas.move(dot, 0, -3)
            root.update()
            root.after(835)

def StartB():
    dot = canvas.create_rectangle(279,182,285,188, fill = "blue", width=2)
    while 1:
        #Leg BC
        for i in range(35):
            canvas.move(dot,-5.25,3)
            root.update()
            root.after(1670)
        #Leg AC
        for i in range(70):
            canvas.move(dot, 0, -3)
            root.update()
            root.after(835)
        #Leg AB
        for i in range(35):
            canvas.move(dot,5.25,3)
            root.update()
            root.after(1800)

def StartC():
    dot = canvas.create_rectangle(97,287,103,293, fill= "blue", width=2)
    while 1:
        #Leg AC
        for i in range(70):
            canvas.move(dot, 0, -3)
            root.update()
            root.after(835)
        #Leg AB
        for i in range(35):
            canvas.move(dot,5.25,3)
            root.update()
            root.after(1800)
        #Leg BC
        for i in range(35):
            canvas.move(dot,-5.25,3)
            root.update()
            root.after(1670)


button1 = Button(frame, text="Start at A", bg="green",command=StartA)
button2 = Button(frame, text="Start at B", bg="green", command = StartB)
button3 = Button(frame, text="Start at C", bg="green", command= StartC)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
    

'''if IMU.getDirection()=="N" and again:
    dot = canvas.create_rectangle(97,287,103,293, fill= "blue", width=2)
    again = False

if IMU.getDirection()=="SE" and again:
    dot = canvas.create_rectangle(97,83,103,77, fill="blue", width=2,)
    again = False
if IMU.direction()=="SW" and again:
    dot = canvas.create_rectangle(279,182,285,188, fill = "blue", width=2)
    again=False'''




root.mainloop()
