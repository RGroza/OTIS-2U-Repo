import Tkinter

top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg="white", height=250, width=300)

coord = 40, 20, 40, 230, 145, 125, 40,20
line = C.create_line(coord, fill="red")

C.pack()
top.mainloop()
