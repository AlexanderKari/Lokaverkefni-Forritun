from tkinter import *
import math,random



def thry():
    for a in root.winfo_children():
        a.destroy()
    def rummal():
        for a in root.winfo_children():
            a.destroy()
        def reikna():

            lengd = float(entry_1.get())
            breidd = float(entry_2.get())
            haed = float(entry_3.get())

            svar = ((lengd * breidd) * haed)/3

            label_4.configure(text = round(svar,2))



        label_1 = Label(root, text = " Sláðu inn Lengd ")
        label_2 = Label(root, text = " Sláðu inn Breidd ")
        label_3 = Label(root, text = " Sláðu inn Hæð ")
        label_4 = Label(root, text = "")
        label_5 = Label(root, text = "Svar:")

        entry_1 = Entry(root, textvariable = StringVar())
        entry_2 = Entry(root, textvariable=StringVar())
        entry_3 = Entry(root, textvariable=StringVar())

        label_1.grid(row = 1, column = 1)
        label_2.grid(row=2, column=1)
        label_3.grid(row=3, column=1)
        label_4.grid(row=4, column=2)
        label_5.grid(row=4, column=1)

        entry_1.grid(row = 1, column = 2)
        entry_2.grid(row=2, column=2)
        entry_3.grid(row=3, column=2)

        button_1 = Button(root, text = " Reikna ", command = reikna)
        button_1.grid(columnspan = 2)

        button_2 = Button(root, text = " Til baka ",command = thry)
        button_2.grid(columnspan = 3)
    def yfirflat():
        for a in root.winfo_children():
            a.destroy()
        def reikna():
            lengd = float(entry_1.get())
            breidd = float(entry_2.get())
            haed = float(entry_3.get())

            svar = lengd * breidd

            c = math.sqrt(math.pow((lengd/2),2)+math.pow(haed,2))
            c2 = math.sqrt(math.pow((breidd / 2), 2) + math.pow(haed, 2))

            svar = svar + (((c * breidd)/2)*2) + (((c2 * lengd)/2)*2)

            label_4.configure(text = round(svar,2))

        label_1 = Label(root, text=" Sláðu inn Lengd ")
        label_2 = Label(root, text=" Sláðu inn Breidd ")
        label_3 = Label(root, text=" Sláðu inn Hæð ")
        label_4 = Label(root, text="")
        label_5 = Label(root, text="Svar:")

        entry_1 = Entry(root, textvariable=StringVar())
        entry_2 = Entry(root, textvariable=StringVar())
        entry_3 = Entry(root, textvariable=StringVar())

        label_1.grid(row=1, column=1)
        label_2.grid(row=2, column=1)
        label_3.grid(row=3, column=1)
        label_4.grid(row=4, column=2)
        label_5.grid(row=4, column=1)

        entry_1.grid(row=1, column=2)
        entry_2.grid(row=2, column=2)
        entry_3.grid(row=3, column=2)

        button_1 = Button(root, text=" Reikna ", command=reikna)
        button_1.grid(columnspan=2)

        button_2 = Button(root, text=" Til baka ", command=thry)
        button_2.grid(columnspan=3)

    def pygor():
        for a in root.winfo_children():
            a.destroy()
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
        # label_1 er texti
        label_1 = Label(root, text="Sláðu inn skammhlið eitt ")
        # label_2 er texti
        label_2 = Label(root, text="Sláðu inn skammhlið tvö ")
        # label_3 er texti
        label_3 = Label(root, text="Sláðu inn langhlið ")
        # label_5 er texti
        label_5 = Label(root, text="Óþekkta hliðin: ")
        # label_6 er texti
        label_6 = Label(root, text="Hliðin sem þú veist ekki slærðu inn 0")
        # texti er mismunadi strengur
        texti = StringVar()
        # texti2 er mismunadi strengur
        texti2 = StringVar()
        # texti3 er mismunadi strengur
        texti3 = StringVar()
        # entry_1 er input sem tekur inn mismunandi streng
        entry_1 = Entry(root, textvariable=texti)
        # entry_2 er input sem tekur inn mismunandi streng
        entry_2 = Entry(root, textvariable=texti2)
        # entry_3 er input sem tekur inn mismunandi streng
        entry_3 = Entry(root, textvariable=texti3)
        # texti er það sem er í entry_1
        texti = entry_1.get()
        # label_4 er tómur texti
        label_4 = Label(root, text="")
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
        button_1 = Button(root, text=" Finna Pyþogoras ", command=py)
        # Staðsetji takkan
        button_1.grid(columnspan=2)

        button_2 = Button(root, text=" Til baka ", command=thry)
        button_2.grid(columnspan=3)

        # Forritið keyrir í loopu

    label_1 = Label(root, text="Veldu hvað þú vilt gera")
    button_1 = Button(root, text=" Rúmmál ", command=rummal)
    button_2 = Button(root, text=" Yfirborðsflatarmál ", command=yfirflat)
    button_3 = Button(root, text=" Pythogoras ", command=pygor)
    button_4 = Button(root, text=" Til baka  ", command=home)

    button_1.grid(row=1, column=1)
    button_2.grid(row=1, column=2)
    button_3.grid(row=1, column=3)
    button_4.grid(row=1, column=4)
    label_1.grid(columnspan=5)

def kula():
    for a in root.winfo_children():
        a.destroy()
    def rummal():
        for a in root.winfo_children():
            a.destroy()
        def reikna():
            radius = float(entry_1.get())


            svar = (4*math.pi*radius**3)/3

            label_2.configure(text=round(svar, 2))

        label_1 = Label(root, text=" Sláðu inn radíus ")
        label_2 = Label(root, text="")
        label_3 = Label(root, text="Svar:")

        entry_1 = Entry(root, textvariable=StringVar())

        label_1.grid(row=1, column=1)
        label_2.grid(row=2, column=2)
        label_3.grid(row=2, column=1)


        entry_1.grid(row=1, column=2)

        button_1 = Button(root, text=" Reikna ", command=reikna)
        button_1.grid(columnspan=2)

        button_2 = Button(root, text=" Til baka ", command=kula)
        button_2.grid(columnspan=3)


    def yfirflat():
        for a in root.winfo_children():
            a.destroy()
        def reikna():
            radius = float(entry_1.get())

            svar = (4 * math.pi * radius ** 2)

            label_2.configure(text=round(svar, 2))

        label_1 = Label(root, text=" Sláðu inn radíus ")
        label_2 = Label(root, text="")
        label_3 = Label(root, text="Svar:")

        entry_1 = Entry(root, textvariable=StringVar())

        label_1.grid(row=1, column=1)
        label_2.grid(row=2, column=2)
        label_3.grid(row=2, column=1)

        entry_1.grid(row=1, column=2)

        button_1 = Button(root, text=" Reikna ", command=reikna)
        button_1.grid(columnspan=2)

        button_2 = Button(root, text=" Til baka ", command=kula)
        button_2.grid(columnspan=3)
    def flatar():
        for a in root.winfo_children():
            a.destroy()
        def reikna():
            radius = float(entry_1.get())

            svar = (math.pi * radius ** 2)

            label_2.configure(text=round(svar, 2))

        label_1 = Label(root, text=" Sláðu inn radíus ")
        label_2 = Label(root, text="")
        label_3 = Label(root, text="Svar:")

        entry_1 = Entry(root, textvariable=StringVar())

        label_1.grid(row=1, column=1)
        label_2.grid(row=2, column=2)
        label_3.grid(row=2, column=1)

        entry_1.grid(row=1, column=2)

        button_1 = Button(root, text=" Reikna ", command=reikna)
        button_1.grid(columnspan=2)

        button_2 = Button(root, text=" Til baka ", command=kula)
        button_2.grid(columnspan=3)


    label_1 = Label(root, text="Veldu hvað þú vilt gera")
    button_1 = Button(root, text=" Rúmmál ", command=rummal)
    button_2 = Button(root, text=" Yfirborðsflatarmál ", command=yfirflat)
    button_3 = Button(root, text=" Flatarmál Hrings ", command=flatar)
    button_4 = Button(root, text=" Til baka  ", command=home)

    button_1.grid(row=1, column=1)
    button_2.grid(row=1, column=2)
    button_3.grid(row=1, column=3)
    button_4.grid(row=1, column=4)
    label_1.grid(columnspan=5)
def kassi():
    for a in root.winfo_children():
        a.destroy()
    def flatar():
        for a in root.winfo_children():
            a.destroy()
        def reikna():
            lengd = float(entry_1.get())
            breidd = float(entry_2.get())

            svar = lengd * breidd

            label_3.configure(text=round(svar, 2))

        label_1 = Label(root, text=" Sláðu inn Lengd ")
        label_2 = Label(root, text=" Sláðu inn Breidd ")
        label_3 = Label(root, text="")
        label_4 = Label(root, text="Svar:")

        entry_1 = Entry(root, textvariable=StringVar())
        entry_2 = Entry(root, textvariable=StringVar())

        label_1.grid(row=1, column=1)
        label_2.grid(row=2, column=1)
        label_4.grid(row=3, column=1)
        label_3.grid(row=3, column=2)

        entry_1.grid(row=1, column=2)
        entry_2.grid(row=2, column=2)

        button_1 = Button(root, text=" Reikna ", command=reikna)
        button_1.grid(columnspan=2)

        button_2 = Button(root, text=" Til baka ", command=kassi)
        button_2.grid(columnspan=3)


    def rummal():
        for a in root.winfo_children():
            a.destroy()

        def reikna():

            lengd = float(entry_1.get())
            breidd = float(entry_2.get())
            haed = float(entry_3.get())

            svar = lengd * breidd * haed

            label_4.configure(text = round(svar,2))
        label_1 = Label(root, text=" Sláðu inn Lengd ")
        label_2 = Label(root, text=" Sláðu inn Breidd ")
        label_3 = Label(root, text=" Sláðu inn Hæð ")
        label_4 = Label(root, text="")
        label_5 = Label(root, text="Svar:")

        entry_1 = Entry(root, textvariable=StringVar())
        entry_2 = Entry(root, textvariable=StringVar())
        entry_3 = Entry(root, textvariable=StringVar())

        label_1.grid(row=1, column=1)
        label_2.grid(row=2, column=1)
        label_3.grid(row=3, column=1)
        label_4.grid(row=4, column=2)
        label_5.grid(row=4, column=1)

        entry_1.grid(row=1, column=2)
        entry_2.grid(row=2, column=2)
        entry_3.grid(row=3, column=2)

        button_1 = Button(root, text=" Reikna ", command=reikna)
        button_1.grid(columnspan=2)

        button_2 = Button(root, text=" Til baka ", command=kassi)
        button_2.grid(columnspan=3)

    def yfirflat():
        for a in root.winfo_children():
            a.destroy()
        def reikna():
            lengd = float(entry_1.get())
            breidd = float(entry_2.get())
            haed = float(entry_3.get())

            hl_1 = lengd * breidd * 2
            hl_2 = lengd * haed *2
            hl_3 = breidd * haed * 2

            svar = hl_1 + hl_2 + hl_3

            label_4.configure(text=round(svar))


        label_1 = Label(root, text=" Sláðu inn Lengd ")
        label_2 = Label(root, text=" Sláðu inn Breidd ")
        label_3 = Label(root, text=" Sláðu inn Hæð ")
        label_4 = Label(root, text="")
        label_5 = Label(root, text="Svar:")

        entry_1 = Entry(root, textvariable=StringVar())
        entry_2 = Entry(root, textvariable=StringVar())
        entry_3 = Entry(root, textvariable=StringVar())

        label_1.grid(row=1, column=1)
        label_2.grid(row=2, column=1)
        label_3.grid(row=3, column=1)
        label_4.grid(row=4, column=2)
        label_5.grid(row=4, column=1)

        entry_1.grid(row=1, column=2)
        entry_2.grid(row=2, column=2)
        entry_3.grid(row=3, column=2)

        button_1 = Button(root, text=" Reikna ", command=reikna)
        button_1.grid(columnspan=2)

        button_2 = Button(root, text=" Til baka ", command=kassi)
        button_2.grid(columnspan=3)



    label_1 = Label(root, text = " Veldu hvað þú vilt gera ")
    button_1 = Button(root, text=" Rúmmál ", command=rummal)
    button_2 = Button(root, text=" Yfirborðsflatarmál ", command=yfirflat)
    button_3 = Button(root, text="Flatarmál ferhyrnings", command=flatar)
    button_4 = Button(root, text=" Til baka ", command=home)

    button_1.grid(row=1, column=1)
    button_2.grid(row=1, column=2)
    button_3.grid(row=1, column=3)
    button_4.grid(row=1, column=4)
    label_1.grid(columnspan=5)

def home():

    for a in root.winfo_children():
        a.destroy()

    label_1 = Label(root, text = "Veldu hvað þú vilt gera")
    button_1 = Button(root, text=" Pýramídi ", command = thry)
    button_2 = Button(root, text=" Kassi ", command = kassi)
    button_3 = Button(root, text=" Kúla ", command = kula)
    button_4 = Button(root, text=" Leikir ", command = leikir)

    button_1.grid(row = 1, column = 1)
    button_2.grid(row = 1, column = 2)
    button_3.grid(row = 1, column = 3)
    button_4.grid(row = 1, column = 4)
    label_1.grid(columnspan=5)

def leikir():
    for a in root.winfo_children():
        a.destroy()
    global Owin
    global Xwin
    global ai
    Owin = 0
    Xwin = 0
    ai = False

    class push:
        def __init__(self):
            for a in root.winfo_children():
                a.destroy()

        def p1():
            global label_p1
            if label_p1 == "   ":
                global tel
                if tel == "X":
                    label_p1 = "X"
                    tel = "O"
                elif tel == "O":
                    label_p1 = "O"
                    tel = "X"
            homeG()

        def p2():
            global label_p2
            if label_p2 == "   ":
                global tel
                if tel == "X":
                    label_p2 = "X"
                    tel = "O"
                elif tel == "O":
                    label_p2 = "O"
                    tel = "X"
            homeG()

        def p3():
            global label_p3
            if label_p3 == "   ":
                global tel
                if tel == "X":
                    label_p3 = "X"
                    tel = "O"
                elif tel == "O":
                    label_p3 = "O"
                    tel = "X"
            homeG()

        def p4():
            global label_p4
            if label_p4 == "   ":
                global tel
                if tel == "X":
                    label_p4 = "X"
                    tel = "O"
                elif tel == "O":
                    label_p4 = "O"
                    tel = "X"
            homeG()

        def p5():
            global label_p5
            if label_p5 == "   ":
                global tel
                if tel == "X":
                    label_p5 = "X"
                    tel = "O"
                elif tel == "O":
                    label_p5 = "O"
                    tel = "X"
            homeG()

        def p6():
            global label_p6
            if label_p6 == "   ":
                global tel
                if tel == "X":
                    label_p6 = "X"
                    tel = "O"
                elif tel == "O":
                    label_p6 = "O"
                    tel = "X"
            homeG()

        def p7():
            global label_p7
            if label_p7 == "   ":
                global tel
                if tel == "X":
                    label_p7 = "X"
                    tel = "O"
                elif tel == "O":
                    label_p7 = "O"
                    tel = "X"
            homeG()

        def p8():
            global label_p8
            if label_p8 == "   ":
                global tel
                if tel == "X":
                    label_p8 = "X"
                    tel = "O"
                elif tel == "O":
                    label_p8 = "O"
                    tel = "X"
            homeG()

        def p9():
            global label_p9
            if label_p9 == "   ":
                global tel
                if tel == "X":
                    label_p9 = "X"
                    tel = "O"
                elif tel == "O":
                    label_p9 = "O"
                    tel = "X"
            homeG()

    class ai_turn:
        def __init__(self):
            for a in root.winfo_children():
                a.destroy()

        def p1():
            global label_p1
            if label_p1 == "   ":
                label_p1 = "O"
                listi.remove(1)
                turn_ai()

        def p2():
            global label_p2
            if label_p2 == "   ":
                label_p2 = "O"
                listi.remove(2)
                turn_ai()

        def p3():
            global label_p3
            if label_p3 == "   ":
                label_p3 = "O"
                listi.remove(3)
                turn_ai()

        def p4():
            global label_p4
            if label_p4 == "   ":
                label_p4 = "O"
                listi.remove(4)
                turn_ai()

        def p5():
            global label_p5
            if label_p5 == "   ":
                label_p5 = "O"
                listi.remove(5)
                turn_ai()

        def p6():
            global label_p6
            if label_p6 == "   ":
                label_p6 = "O"
                listi.remove(6)
                turn_ai()

        def p7():
            global label_p7
            if label_p7 == "   ":
                label_p7 = "O"
                listi.remove(7)
                turn_ai()

        def p8():
            global label_p8
            if label_p8 == "   ":
                label_p8 = "O"
                listi.remove(8)
                turn_ai()

        def p9():
            global label_p9
            if label_p9 == "   ":
                label_p9 = "O"
                listi.remove(9)
                turn_ai()

    def turn_ai():
        global listi
        global label_p1
        global label_p2
        global label_p3
        global label_p4
        global label_p5
        global label_p6
        global label_p7
        global label_p8
        global label_p9
        try:
            val = random.choice(listi)
            if (label_p1 == "O" and label_p2 == "O" and label_p3 == "O") or (
                        label_p4 == "O" and label_p5 == "O" and label_p6 == "O") or (
                        label_p7 == "O" and label_p8 == "O" and label_p9 == "O") or (
                        label_p1 == "O" and label_p4 == "O" and label_p7 == "O") or (
                        label_p2 == "O" and label_p5 == "O" and label_p8 == "O") or (
                        label_p3 == "O" and label_p6 == "O" and label_p9 == "O") or (
                        label_p1 == "O" and label_p5 == "O" and label_p9 == "O") or (
                        label_p3 == "O" and label_p5 == "O" and label_p7 == "O"):
                homeG()
            elif val == 1:
                label_p1 = "X"
            elif val == 2:
                label_p2 = "X"
            elif val == 3:
                label_p3 = "X"
            elif val == 4:
                label_p4 = "X"
            elif val == 5:
                label_p5 = "X"
            elif val == 6:
                label_p6 = "X"
            elif val == 7:
                label_p7 = "X"
            elif val == 8:
                label_p8 = "X"
            elif val == 9:
                label_p9 = "X"
            listi.remove(val)
        except:
            homeG()
        homeG()

    def reset():
        global listi
        listi = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        global tel
        tel = "O"

        global label_p1
        label_p1 = "   "

        global label_p2
        label_p2 = "   "

        global label_p3
        label_p3 = "   "

        global label_p4
        label_p4 = "   "

        global label_p5
        label_p5 = "   "

        global label_p6
        label_p6 = "   "

        global label_p7
        label_p7 = "   "

        global label_p8
        label_p8 = "   "

        global label_p9
        label_p9 = "   "

        homeG()

    def vinner(x):
        for a in root.winfo_children():
            a.destroy()
        r1c1 = Button(root, text=label_p1, command="")
        r1c2 = Button(root, text=label_p2, command="")
        r1c3 = Button(root, text=label_p3, command="")
        r2c1 = Button(root, text=label_p4, command="")
        r2c2 = Button(root, text=label_p5, command="")
        r2c3 = Button(root, text=label_p6, command="")
        r3c1 = Button(root, text=label_p7, command="")
        r3c2 = Button(root, text=label_p8, command="")
        r3c3 = Button(root, text=label_p9, command="")
        label = Label(root, text=x)
        res = Button(root, text="Reset", command=reset)
        haetta = Button(root, text ="Hætta",command=leikir)

        r1c1.grid(row=1, column=1)
        r1c2.grid(row=1, column=2)
        r1c3.grid(row=1, column=3)
        r2c1.grid(row=2, column=1)
        r2c2.grid(row=2, column=2)
        r2c3.grid(row=2, column=3)
        r3c1.grid(row=3, column=1)
        r3c2.grid(row=3, column=2)
        r3c3.grid(row=3, column=3)
        label.grid(columnspan=5)
        res.grid(columnspan=5)
        haetta.grid(columnspan=5)

    def tolva():
        global ai
        ai = True
        homeG()

    def leikmann():
        global ai
        ai = False
        homeG()

    def homeT():
        for a in root.winfo_children():
            a.destroy()
        button_1 = Button(root, text="Tölva", command=tolva)
        button_2 = Button(root, text="Leikmann", command=leikmann)
        label = Label(root, text="Veldu hvor þú vilt spila á móti")

        label.grid(columnspan=3)
        button_1.grid(row=1, column=1)
        button_2.grid(row=1, column=2)

    def homeG():
        for a in root.winfo_children():
            a.destroy()
        if ai == False:
            r1c1 = Button(root, text=label_p1, command=push.p1)
            r1c2 = Button(root, text=label_p2, command=push.p2)
            r1c3 = Button(root, text=label_p3, command=push.p3)
            r2c1 = Button(root, text=label_p4, command=push.p4)
            r2c2 = Button(root, text=label_p5, command=push.p5)
            r2c3 = Button(root, text=label_p6, command=push.p6)
            r3c1 = Button(root, text=label_p7, command=push.p7)
            r3c2 = Button(root, text=label_p8, command=push.p8)
            r3c3 = Button(root, text=label_p9, command=push.p9)
        elif ai == True:
            r1c1 = Button(root, text=label_p1, command=ai_turn.p1)
            r1c2 = Button(root, text=label_p2, command=ai_turn.p2)
            r1c3 = Button(root, text=label_p3, command=ai_turn.p3)
            r2c1 = Button(root, text=label_p4, command=ai_turn.p4)
            r2c2 = Button(root, text=label_p5, command=ai_turn.p5)
            r2c3 = Button(root, text=label_p6, command=ai_turn.p6)
            r3c1 = Button(root, text=label_p7, command=ai_turn.p7)
            r3c2 = Button(root, text=label_p8, command=ai_turn.p8)
            r3c3 = Button(root, text=label_p9, command=ai_turn.p9)
        res = Button(root, text="Reset", command=reset)
        global Owin
        global Xwin
        lable_O = Label(root, text="Sigrar O: " + str(Owin))
        lable_X = Label(root, text="Sigrar X: " + str(Xwin))

        r1c1.grid(row=1, column=1)
        r1c2.grid(row=1, column=2)
        r1c3.grid(row=1, column=3)
        r2c1.grid(row=2, column=1)
        r2c2.grid(row=2, column=2)
        r2c3.grid(row=2, column=3)
        r3c1.grid(row=3, column=1)
        r3c2.grid(row=3, column=2)
        r3c3.grid(row=3, column=3)
        res.grid(columnspan=4)
        lable_O.grid(row=1, column=4)
        lable_X.grid(row=2, column=4)

        if (label_p1 == "X" and label_p2 == "X" and label_p3 == "X") or (
                    label_p4 == "X" and label_p5 == "X" and label_p6 == "X") or (
                    label_p7 == "X" and label_p8 == "X" and label_p9 == "X") or (
                    label_p1 == "X" and label_p4 == "X" and label_p7 == "X") or (
                    label_p2 == "X" and label_p5 == "X" and label_p8 == "X") or (
                    label_p3 == "X" and label_p6 == "X" and label_p9 == "X") or (
                    label_p1 == "X" and label_p5 == "X" and label_p9 == "X") or (
                    label_p3 == "X" and label_p5 == "X" and label_p7 == "X"):
            vinner("X Vinnur!")
            Xwin += 1
        elif (label_p1 == "O" and label_p2 == "O" and label_p3 == "O") or (
                    label_p4 == "O" and label_p5 == "O" and label_p6 == "O") or (
                    label_p7 == "O" and label_p8 == "O" and label_p9 == "O") or (
                    label_p1 == "O" and label_p4 == "O" and label_p7 == "O") or (
                    label_p2 == "O" and label_p5 == "O" and label_p8 == "O") or (
                    label_p3 == "O" and label_p6 == "O" and label_p9 == "O") or (
                    label_p1 == "O" and label_p5 == "O" and label_p9 == "O") or (
                    label_p3 == "O" and label_p5 == "O" and label_p7 == "O"):
            vinner("O Vinnur!")
            Owin += 1
        elif label_p1 != "   " and label_p2 != "   " and label_p3 != "   " and label_p4 != "   " and label_p5 != "   " and label_p6 != "   " and label_p7 != "   " and label_p8 != "   " and label_p9 != "   ":
            vinner("Enginn Vinnur")


    def mylla():
        reset()
        homeT()
    def sbs():
        for a in root.winfo_children():
            a.destroy()
        button_1 = Button(root, text="Skæri", command = skaeri)
        button_2 = Button(root, text="Blað", command = blad)
        button_3 = Button(root, text="Steinn", command = steinn)

        button_1.grid(row=1,column=1)
        button_2.grid(row=2, column=1)
        button_3.grid(row=3, column=1)


    label_1 = Label(root, text="Veldu hvað þú vilt gera")
    button_1 = Button(root, text=" Skæri, blað, steinn ", command=sbs)
    button_2 = Button(root, text=" Mylla ", command=mylla)
    button_3 = Button(root, text=" *Unactive* ", command="")
    button_4 = Button(root, text=" Til baka ", command=home)

    button_1.grid(row=1, column=1)
    button_2.grid(row=1, column=2)
    button_3.grid(row=1, column=3)
    button_4.grid(row=1, column=4)
    label_1.grid(columnspan=5)



root = Tk()
home()

root.mainloop()
