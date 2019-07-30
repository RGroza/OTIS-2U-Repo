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


class MyWidget(GridLayout):
    def __init__(self,**kwargs):
        super(MyWidget,self).__init__(**kwargs)
        self.cols = 2
        self.inside = GridLayout()
        self.go = Button(text="GO")
        self.go.bind(on_press=self.getGo)
        self.add_widget(self.go)
        self.add_widget(Label(text="Time: "))
        self.time = self.getTime()
        self.add_widget(Label(text=self.time))
        self.add_widget(Label(text="Position: "))
        self.posit = self.getPosit()
        self.add_widget(Label(text=self.posit))
        self.reset = Button(text="Reset")
        self.reset.bind(on_press=self.getReset)
        self.add_widget(self.reset)
        self.image = Button(text="Images")
        self.image.bind(on_release=self.getImage)
        self.add_widget(self.image)
        
    def getImage(self, instance):
        show_popup()
    def getTime(self):
        return " "
    def getPosit(self):
        return " "
    def getReset(self, instance):
        print ("test")
    def getGo(self, instance):
        print ("test")
class P(FloatLayout):
    pass    
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
