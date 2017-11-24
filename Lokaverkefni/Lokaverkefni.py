from tkinter import *
import math



root = Tk()
label_1 = Label(root, text = "Veldu hvað þú vilt gera")
button_1 = Button(root, text=" Finna Pyþogoras ", command="")
button_2 = Button(root, text=" sgsg", command = "")
button_3 = Button(root, text=" sgsg", command = "")
button_4 = Button(root, text=" sgsg", command = "")

button_1.grid(row = 1, column = 1)
button_2.grid(row = 1, column = 2)
button_3.grid(row = 1, column = 3)
button_4.grid(row = 1, column = 4)
label_1.grid(columnspan=5)
root.mainloop()

