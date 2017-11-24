from tkinter import *
import math

def pygor():
    root.destroy()
    def py():
        # tala1 er það sem er í entry_1
        tala1 = float(entry_1.get())
        # tala2 er það sem er í entry_2
        tala2 = float(entry_2.get())
        # tala3 er það sem er í entry_3
        tala3 = float(entry_3.get())
        # Ef tala1 og tala2 og tala3 eru meira en 0
        if tala1 > 0 and tala2 > 0 and tala3 > 0:
            # Breyti hvað er í lable_4 og set strengin
            label_4.configure(text="Ein hlið þarf að vera óþekkt")
        # Ef einhverjar tvær tölur eru 0
        elif (tala1 == 0 and tala2 == 0) or (tala1 == 0 and tala3 == 0) or (tala2 == 0 and tala3 == 0):
            # Breyti hvað er í lable_4 og set strengin
            label_4.configure(text="Villa meiri en ein hlið er með lengdina 0")
        # Ef tala3 er meira en 0 en minna en annhvort tala1 eða tala2
        elif (tala3 <= tala1 or tala3 <= tala2) and tala3 > 0:
            # Breyti hvað er í lable_4 og set strengin
            label_4.configure(text="Langhlið getur ekki verið minni eða sama og skammhlið")

        # Ef tala3 er 0
        elif tala3 == 0:
            # Reikna pýþagóras
            utkoma = math.sqrt((math.pow(tala1, 2)) + (math.pow(tala2, 2)))
            # Breyti hvað er í lable_4 og set utkoma
            label_4.configure(text=round(utkoma, 2))
        elif tala2 == 0:
            # Reikna pýþagóras
            utkoma = math.sqrt((math.pow(tala3, 2)) - (math.pow(tala1, 2)))
            # Breyti hvað er í lable_4 og set utkoma
            label_4.configure(text=round(utkoma, 2))
        elif tala1 == 0:
            # Reikna pýþagóras
            utkoma = math.sqrt((math.pow(tala3, 2)) - (math.pow(tala2, 2)))
            # Breyti hvað er í lable_4 og set utkoma
            label_4.configure(text=round(utkoma, 2))
    global P
    P = Tk()  # auður gluggi
    # label_1 er texti
    label_1 = Label(P, text="Sláðu inn skammhlið eitt ")
    # label_2 er texti
    label_2 = Label(P, text="Sláðu inn skammhlið tvö ")
    # label_3 er texti
    label_3 = Label(P, text="Sláðu inn langhlið ")
    # label_5 er texti
    label_5 = Label(P, text="Óþekkta hliðin: ")
    # label_6 er texti
    label_6 = Label(P, text="Hliðin sem þú veist ekki slærðu inn 0")
    # texti er mismunadi strengur
    texti = StringVar()
    # texti2 er mismunadi strengur
    texti2 = StringVar()
    # texti3 er mismunadi strengur
    texti3 = StringVar()
    # entry_1 er input sem tekur inn mismunandi streng
    entry_1 = Entry(P, textvariable=texti)
    # entry_2 er input sem tekur inn mismunandi streng
    entry_2 = Entry(P, textvariable=texti2)
    # entry_3 er input sem tekur inn mismunandi streng
    entry_3 = Entry(P, textvariable=texti3)
    # texti er það sem er í entry_1
    texti = entry_1.get()
    # label_4 er tómur texti
    label_4 = Label(P, text="")
    # Stað set öll stök(strengi,inputs...)
    label_6.grid(columnspan=2)
    label_1.grid(row=1, sticky=E)
    label_2.grid(row=2, sticky=E)
    label_3.grid(row=3, sticky=E)
    label_5.grid(row=4, sticky=E)
    entry_1.grid(row=1, column=1)
    entry_2.grid(row=2, column=1)
    entry_3.grid(row=3, column=1)
    label_4.grid(row=4, column=1)


    # button_1 er takki sem kallar á fallið py
    button_1 = Button(P, text=" Finna Pyþogoras ", command=py)
    # Staðsetji takkan
    button_1.grid(columnspan=2)

    button_2 = Button(P, text=" Fara til baka ", command=home)
    button_2.grid(columnspan=3)

    # Forritið keyrir í loopu
    P.mainloop()

def home():
    try:
        P.destroy()
    except:
        print("P ekki til")
    global root
    root = Tk()
    label_1 = Label(root, text = "Veldu hvað þú vilt gera")
    button_1 = Button(root, text=" Finna Pyþogoras ", command=pygor)
    button_2 = Button(root, text=" sgsg ", command = "")
    button_3 = Button(root, text=" sgsg ", command = "")
    button_4 = Button(root, text=" sgsg ", command = "")

    button_1.grid(row = 1, column = 1)
    button_2.grid(row = 1, column = 2)
    button_3.grid(row = 1, column = 3)
    button_4.grid(row = 1, column = 4)
    label_1.grid(columnspan=5)
    root.mainloop()

home()