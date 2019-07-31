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


class MyWidget(GridLayout):
    def __init__(self,**kwargs):
        super(MyWidget,self).__init__(**kwargs)
        
        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.add_widget(Label(text="Time: "))
        self.time = Label(text=" ")
        self.inside.add_widget(self.time)
        self.inside.add_widget(Label(text="Position: "))
        self.posit = Label(text=" ")
        self.inside.add_widget(self.posit)
        self.inside.add_widget(Label(text="Battery Percentage: "))
        self.percent = Label(text=" ")
        self.inside.add_widget(self.percent)
        self.inside.add_widget(Label(text="Battery Voltage: "))
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
    def getBattPercent(self):
        file=open("telemetry0.txt", "r")
        content=file.readlines()
        self.percent = content[67:80]
    def getPanel1(self):
        file=open("telemetry0.txt", "r")
        content=file.readlines()
        self.panel1=content[96:99]
    def getPanel2(self):
        file=open("telemetry0.txt", "r")
        content=file.readlines()
        self.panel2=content[96:99]
    def getPanel3(self):
        file=open("telemetry0.txt", "r")
        content=file.readlines()
        self.panel3=content[96:99]
    def getPanel4(self):
        file=open("telemetry0.txt", "r")
        content=file.readlines()
        self.panel4=content[96:99]
    def getReset(self, instance):
        print ("test")
    def getGo(self, instance):
        self.getBattPercent()
        self.getPanel1()
        self.getPanel2()
        self.getPanel3()
        self.getPanel4()
        
class P(FloatLayout):
    def btn1(self):
        file=open("telemetry0.txt", "r")
        content=file.readlines()
        print ("Picture: " + content[8:9])
        print ("Oxidation %: " + content[16:33])
    def btn2(self):
        file=open("telemetry0.txt", "r")
        content=file.readlines()
        print ()
    def btn3(self):
        file=open("telemetry0.txt", "r")
        content=file.readlines()
        print ("")
    def btn4(self):
        file=open("telemetry0.txt", "r")
        content=file.readlines()
        print ("")
    def btn5(self):
        file=open("telemetry0.txt", "r")
        content=file.readlines()
        print ("")
    
class Otis(App):
    def build(self):
        return MyWidget()

def show_popup():
    show = P()
    popupWindow = Popup(title="OTIS", content=show, size_hint=(None,None), size=(400,400))
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
