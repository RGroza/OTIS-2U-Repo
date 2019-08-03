import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import time
from PIL import Image


class MyWidget(GridLayout):
    def __init__(self,**kwargs):
        super(MyWidget,self).__init__(**kwargs)
        
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.add_widget(Label(text="Time: "))
        self.time = Label(text="14:35")
        self.inside.add_widget(self.time)
        self.inside.add_widget(Label(text="Position: "))
        self.posit = Label(text="N")
        self.inside.add_widget(self.posit)
        self.inside.add_widget(Label(text="Battery Charge: "))
        self.percent = Label(text=" ")
        self.inside.add_widget(self.percent)
        self.inside.add_widget(Label(text="CubeSat Temperature: "))
        self.volt = Label(text=" ")
        self.inside.add_widget(self.volt)
        self.inside.add_widget(Label(text="Solar Panel 1: "))
        self.panel1 = Label(text=" ")
        self.inside.add_widget(self.panel1)
        self.inside.add_widget(Label(text="Solar Panel 2: "))
        self.panel2 = Label(text=" ")
        self.inside.add_widget(self.panel2)
        self.inside.add_widget(Label(text="Solar Panel 3: "))
        self.panel3 = Label(text=" ")
        self.inside.add_widget(self.panel3)
        self.inside.add_widget(Label(text="Solar Panel 4: "))
        self.panel4 = Label(text=" ")
        self.inside.add_widget(self.panel4)
        self.add_widget(self.inside)
        self.go = Button(text="Refresh")
        self.go.bind(on_press=self.getGo)
        self.add_widget(self.go)
        self.reset = Button(text="Reset")
        self.reset.bind(on_press=self.getReset)
        self.add_widget(self.reset)
        self.image = Button(text="Images")
        self.image.bind(on_release=self.getImage)
        self.add_widget(self.image)
        
    
    def getImage(self, instance):
        show_popup()
    def getBattPercent(self, mydir):
        file=open(str(mydir) + "telemetry.txt", "r")
        content=file.readlines()
        self.percent.text = content[10]
        file.close()
    def getTemp(self, mydir):
        file=open(str(mydir) + "telemetry.txt", "r")
        content=file.readlines()
        self.volt.text = content[11]
        file.close()
    def getPanel1(self, mydir):
        file=open(str(mydir) + "telemetry.txt", "r")
        content=file.readlines()
        self.panel1.text=content[12]
        file.close()
    def getPanel2(self, mydir):
        file=open(str(mydir) + "telemetry.txt", "r")
        content=file.readlines()
        self.panel2.text=content[13]
        file.close()
    def getPanel3(self, mydir):
        file=open(str(mydir) + "telemetry.txt", "r")
        content=file.readlines()
        self.panel3.text=content[14]
        file.close()
    def getPanel4(self, mydir):
        file=open(str(mydir) + "telemetry.txt", "r")
        content=file.readlines()
        self.panel4.text=content[15]
        file.close()
    def getReset(self, instance):
        print ("test")
    def getGo(self, instance):
        mydir = 'C:/Work/BWSI/CubeSats/sat_images/'
        self.getTemp(mydir)
        self.getBattPercent(mydir)
        self.getPanel1(mydir)
        self.getPanel2(mydir)
        self.getPanel3(mydir)
        self.getPanel4(mydir)
        
class P(FloatLayout):
    def btn1(self, mydir):
        file=open(str(mydir) + "telemetry.txt", "r")
        content=file.readlines()
        self.ids.lab1.text = ("Picture: " + content[1] + "Oxidation %: " + content[0])
        #image1 = Image.open(content[1] + ".png")
        #self.ids.im1.source = image1
        file.close()
    def btn2(self, mydir):
        file=open(str(mydir) + "telemetry.txt", "r")
        content=file.readlines()
        self.ids.lab2.text = ("Picture: " + content[3] + "Oxidation %: " + content[2])
        file.close()
    def btn3(self, mydir):
        file=open(str(mydir) + "telemetry.txt", "r")
        content=file.readlines()
        self.ids.lab3.text = ("Picture: " + content[5] + "Oxidation %: " + content[4])
        #self.ids.im3.source = (str(content[5]) + ".png")
        file.close()
    def btn4(self, mydir):
        file=open(str(mydir) + "telemetry.txt", "r")
        content=file.readlines()
        self.ids.lab4.text = ("Picture: " + content[7] + "Oxidation %: " + content[6])
        file.close()
    def btn5(self, mydir):
        file=open(str(mydir) + "telemetry.txt", "r")
        content=file.readlines()
        self.ids.lab5.text = ("Picture: " + content[9] + "Oxidation %: " + content[8])
        file.close()
    
class Otis(App):
    def build(self):
        return MyWidget()

def show_popup():
    show = P()
    popupWindow = Popup(title="OTIS", content=show, size_hint=(None,None), size=(600,400))
    popupWindow.open()

if __name__ == "__main__":
    Otis().run()
    
    #def __init__ (self, **kwargs):
     #   super(Grid, self).__init__(**kwargs)
        
      #  self.cols=1
       #self.inside.cols = 2
        
        
        #self.inside.add_widget(Label(text="Name: "))
        #self.name=TextInput(multiline=False)
        #self.inside.add_widget(self.name)
        
        #self.add_widget(self.inside)
        
        #self.submit = Button(text="Submit", font_size=40)
        #self.submit.bind(on_press=self.pressed)
        #self.add_widget(self.submit)
    #def pressed(self, instance):
        #name = self.name.text
        
        #print(name)
        #self.name.text = ""

#import Tkinter

#top = Tkinter.Tk()

#C = Tkinter.Canvas(top, bg="white", height=250, width=300)

#coord = 40, 20, 40, 230, 145, 125, 40,20
#line = C.create_line(coord, fill="red")

#C.pack()
#top.mainloop()
