from tkinter import *
import math,random


#Fall sem heldur utan um þríhyrninga liðinn
def thry():
    for a in root.winfo_children():
        a.destroy()
    #Fall sem reiknar rúmmál þríhyrnings
    def rummal():
        for a in root.winfo_children():
            a.destroy()
        #Fall sem framkvæmir reikni aðgerðina
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
    #Fall sem reiknar yfirflatarmál
    def yfirflat():
        for a in root.winfo_children():
            a.destroy()
        #Fall sem framkvæmir reikni aðgerðina
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
    #Fall sem reiknar pythogoras
    def pygor():
        for a in root.winfo_children():
            a.destroy()
        #Fall sem framkvæmir reikni aðgerðina
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
#Fall sem heldur utan um kúlu liðinn
def kula():
    for a in root.winfo_children():
        a.destroy()
    #Fall sem reiknar rúmmál
    def rummal():
        for a in root.winfo_children():
            a.destroy()
        #Fall sem framkvæmir reikni aðgerðina
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

    #Fall sem reiknar yfirborðsflatarmál
    def yfirflat():
        for a in root.winfo_children():
            a.destroy()
        #Fall sem framkvæmir reikni aðgerðina
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
    #Fall sem reiknar flatarmál
    def flatar():
        for a in root.winfo_children():
            a.destroy()
        #Fall sem framvæmir reikni aðgerðina
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
#Fall sem heldur utan um kassa liðinn
def kassi():
    for a in root.winfo_children():
        a.destroy()
    #Fall sem reiknar flatarmál
    def flatar():
        for a in root.winfo_children():
            a.destroy()
        #Fall sem framkvæmir reikni aðgerðina
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

    #Fall sem reiknar rúmmál
    def rummal():
        for a in root.winfo_children():
            a.destroy()
        #Fall sem framkvæmir reikni aðgerðina
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
    #Fall er reiknar yfirborðsflatarmál
    def yfirflat():
        for a in root.winfo_children():
            a.destroy()
        #Fall sem framkvæmir reikni aðgerðina
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
#Fall sem heldur utan um home
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
#Fall sem heldur utan um leikina
def leikir():
    for a in root.winfo_children():
        a.destroy()
    global Owin
    global Xwin
    global ai
    Owin = 0
    Xwin = 0
    ai = False
    #Klasi sem keyrir þegar er ýtt á takka í myllu
    class push:
        def __init__(self):
            for a in root.winfo_children():
                a.destroy()
        #Ef valið var takka 1
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

        # Ef valið var takka 2
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

        # Ef valið var takka 3
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

        # Ef valið var takka 4
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

        # Ef valið var takka 5
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

        # Ef valið var takka 6
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

        # Ef valið var takka 7
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

        # Ef valið var takka 8
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

        # Ef valið var takka 9
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
    #Klasi fyrir ef þú ert að spila á móti tölvunni
    class ai_turn:
        def __init__(self):
            for a in root.winfo_children():
                a.destroy()

        # Ef valið var takka 1
        def p1():
            global label_p1
            if label_p1 == "   ":
                label_p1 = "O"
                listi.remove(1)
                turn_ai()

        # Ef valið var takka 2
        def p2():
            global label_p2
            if label_p2 == "   ":
                label_p2 = "O"
                listi.remove(2)
                turn_ai()

        # Ef valið var takka 3
        def p3():
            global label_p3
            if label_p3 == "   ":
                label_p3 = "O"
                listi.remove(3)
                turn_ai()

        # Ef valið var takka 4
        def p4():
            global label_p4
            if label_p4 == "   ":
                label_p4 = "O"
                listi.remove(4)
                turn_ai()

        # Ef valið var takka 5
        def p5():
            global label_p5
            if label_p5 == "   ":
                label_p5 = "O"
                listi.remove(5)
                turn_ai()

        # Ef valið var takka 6
        def p6():
            global label_p6
            if label_p6 == "   ":
                label_p6 = "O"
                listi.remove(6)
                turn_ai()

        # Ef valið var takka 7
        def p7():
            global label_p7
            if label_p7 == "   ":
                label_p7 = "O"
                listi.remove(7)
                turn_ai()

        # Ef valið var takka 8
        def p8():
            global label_p8
            if label_p8 == "   ":
                label_p8 = "O"
                listi.remove(8)
                turn_ai()

        # Ef valið var takka 9
        def p9():
            global label_p9
            if label_p9 == "   ":
                label_p9 = "O"
                listi.remove(9)
                turn_ai()

    #Fall fyrir tölvuna að gera
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
        #Reyni
        try:
            val = random.choice(listi)
            #Ef notandi er búin að vinna
            if (label_p1 == "O" and label_p2 == "O" and label_p3 == "O") or (
                        label_p4 == "O" and label_p5 == "O" and label_p6 == "O") or (
                        label_p7 == "O" and label_p8 == "O" and label_p9 == "O") or (
                        label_p1 == "O" and label_p4 == "O" and label_p7 == "O") or (
                        label_p2 == "O" and label_p5 == "O" and label_p8 == "O") or (
                        label_p3 == "O" and label_p6 == "O" and label_p9 == "O") or (
                        label_p1 == "O" and label_p5 == "O" and label_p9 == "O") or (
                        label_p3 == "O" and label_p5 == "O" and label_p7 == "O"):
                vinner("O vinnur!")
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
        #Annars
        except:
            homeG()
        homeG()
    #Fall tuk að reseta leikinn
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
    #Fall þegar einhver er búin að vinna
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
    #Fall ef valið er að spila á móti tölvu
    def tolva():
        global ai
        ai = True
        homeG()

    # Fall ef valið er að spila á móti leikmann
    def leikmann():
        global ai
        ai = False
        homeG()

    # Fall sem spyr þig hvor þú vil spila á móti tölvu eða leikmann
    def homeT():
        for a in root.winfo_children():
            a.destroy()
        button_1 = Button(root, text="Tölva", command=tolva)
        button_2 = Button(root, text="Leikmann", command=leikmann)
        label = Label(root, text="Veldu hvor þú vilt spila á móti")

        label.grid(columnspan=3)
        button_1.grid(row=1, column=1)
        button_2.grid(row=1, column=2)
    #Aðal heimaskjár myllu
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

    #Fall sem byrjar myllu
    def mylla():
        reset()
        homeT()
    #Fall sem heldur utan um leikinn Planets
    def Planets():
        #Fall sem resetar leikinn
        def reset():
            for a in root.winfo_children():
                a.destroy()
            global dot
            global canvas
            global Sx
            global Sy
            global wW
            global wH
            global fY
            global speed
            global room
            global oldroom
            global Cy
            global Cx
            global star
            global Seaty
            global Seatx
            global sol
            global dod
            global tel
            global planets
            global rooms
            global Dx
            global Dy
            global Dr
            global fuel
            global maxfuel
            global eydsla
            global Etel

            Sx = 200
            Sy = 200

            wW = 1200
            wH = 900

            Seaty = wH / 2
            Seatx = 800

            Cx = Seatx
            Cy = Seaty

            fY = "a"

            tel = 0

            speed = 7

            planets = []
            star = []

            rooms = ["R1", "R2", "R3", "R4"]
            oldroom = ""

            Dx = random.randint(10, 600)
            Dy = random.randint(10, 600)
            Dr = "R1"

            maxfuel = 100
            fuel = 100
            eydsla = 20
            Etel = 1

            sol = []

            dod = False

            canvas = Canvas(root, width=wW, height=wH, borderwidth=0, highlightthickness=0, bg="black")
            dot = canvas.create_circle(Dx, Dy, 3, fill="yellow")
            stars(500, 10, 10, wW, wH)

            R1()

            canvas.bind("<Key>", key)
            canvas.bind("<Button-1>", callback)
            canvas.pack()
            root.wm_title("Planets")

            homeS()

        # Svo það er þæginlegt að búa til hringi
        def _create_circle(self, x, y, r, **kwargs):
            global canvas
            return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)

        # Til að geta notað command til að búa til hring
        Canvas.create_circle = _create_circle

        # Svo það er þæginlegt að búa til pizzu form
        def _create_circle_arc(self, x, y, r, **kwargs):
            global canvas
            if "start" in kwargs and "end" in kwargs:
                kwargs["extent"] = kwargs["end"] - kwargs["start"]
                del kwargs["end"]
            return self.create_arc(x - r, y - r, x + r, y + r, **kwargs)

        # Til að geta notað command til að búa til pizzu form
        Canvas.create_circle_arc = _create_circle_arc

        # Þegar er ýtt á takka er farið hér
        def key(event):
            global canvas
            global listi
            for a in listi:
                canvas.delete(a)
            print("pressed", repr(event.char))
            global fuel
            global maxfuel
            global eydsla
            global Etel
            global Sx
            global Sy
            global wW
            global wH
            global fY
            global speed
            global room
            global oldroom
            global Cy
            global Cx
            global star
            global Seaty
            global Seatx
            global sol
            global dod
            if event.char == "q":
                if room == "sR1" and Cx == Seatx and Cy == Seaty:
                    if oldroom == "R1":
                        R1()
                    elif oldroom == "R2":
                        R2()
                    elif oldroom == "R3":
                        R3()
                    elif oldroom == "R4":
                        R4()
                elif room != "sR1" and room != "sR2" and room != "sR3":
                    oldroom = room
                    sR1()
            if room == "sR1" or room == "sR2" or room == "sR3":
                if event.char == "w":
                    if Cy > 254:
                        Cy -= speed
                elif event.char == "s":
                    if Cy < wH - 254:
                        Cy += speed
                elif event.char == "a":
                    if room != "sR3":
                        if Cx > 50:
                            Cx -= speed
                        else:
                            if room == "sR2":
                                sR3()
                            elif room == "sR1":
                                sR2()
                            Cx = wW
                    else:
                        if Cx > 303 + 50:
                            Cx -= speed
                elif event.char == "d":
                    if room != "sR1":
                        if Cx < wW - 50:
                            Cx += speed
                        else:
                            if room == "sR2":
                                sR1()
                            elif room == "sR3":
                                sR2()
                            Cx = 2
                    else:
                        if Cx < 934 - 50:
                            Cx += speed

            else:
                if Etel % eydsla == 0:
                    fuel = fuel - 1
                Etel += 1
                if event.char == "w":
                    if Sy > 8:
                        Sy -= speed
                        fY = "w"
                    else:
                        if room == "R3":
                            R1()
                            Sy = wH
                        elif room == "R4":
                            R2()
                            Sy = wH
                elif event.char == "s":
                    if Sy < wH - 6:
                        Sy += speed
                        fY = "s"
                    else:
                        if room == "R1":
                            R3()
                            Sy = 0
                        elif room == "R2":
                            R4()
                            Sy = 0
                elif event.char == "a":
                    if Sx > 8:
                        Sx -= speed
                        fY = "a"
                    else:
                        if room == "R2":
                            R1()
                            Sx = wW
                        elif room == "R4":
                            R3()
                            Sx = wW
                elif event.char == "d":
                    if Sx < wW - 6:
                        Sx += speed
                        fY = "d"
                    else:
                        if room == "R1":
                            R2()
                            Sx = 0
                        elif room == "R3":
                            R4()
                            Sx = 0
                for a in sol:
                    canvas.delete(a)
                inn = False
                if room == "R1":
                    tel = 0
                    for a in range(628):
                        if Sy > round(900 + 400 * math.sin(tel)) and Sx > round(
                                        1200 + 400 * math.cos(tel)):  # 1200, 900
                            inn = True
                        if Sy > round(900 + 300 * math.sin(tel)) and Sx > round(1200 + 300 * math.cos(tel)):
                            dod = True
                            break
                        tel = round(tel + 0.01, 2)
                elif room == "R2":
                    tel = 0
                    for a in range(628):
                        if Sy > round(900 + 400 * math.sin(tel)) and Sx < round(0 + 400 * math.cos(tel)):  # 0, 900
                            inn = True
                        if Sy > round(900 + 300 * math.sin(tel)) and Sx < round(0 + 300 * math.cos(tel)):
                            dod = True
                            break
                        tel = round(tel + 0.01, 2)
                elif room == "R3":
                    tel = 0
                    for a in range(628):
                        if Sy < round(0 + 400 * math.sin(tel)) and Sx > round(1200 + 400 * math.cos(tel)):  # 1200, 0
                            inn = True
                        if Sy < round(0 + 300 * math.sin(tel)) and Sx > round(1200 + 300 * math.cos(tel)):
                            dod = True
                            break
                        tel = round(tel + 0.01, 2)
                elif room == "R4":
                    tel = 0
                    for a in range(628):
                        if Sy < round(0 + 400 * math.sin(tel)) and Sx < round(0 + 400 * math.cos(tel)):  # 0, 0
                            inn = True
                        if Sy < round(0 + 300 * math.sin(tel)) and Sx < round(0 + 300 * math.cos(tel)):
                            dod = True
                            break
                        tel = round(tel + 0.01, 2)
                if inn == True:
                    if dod == True:
                        for a in sol:
                            canvas.delete(a)
                        destroy(15)
                    elif dod == False:
                        sol.append(canvas.create_text(wW / 2, wH / 2, text="Heat Warning!", fill="white"))
            if room == "sR1" or room == "sR2" or room == "sR3":
                homeSS()
            else:
                homeS()
        #Fall fyrir ef þú ert bensínlaus
        def emty():
            global dod
            global sol
            dod = True
            canvas.bind("<Key>", dead)
            for a in sol:
                canvas.delete(a)
            user()
            canvas.create_text(wW / 2, wH / 2, text="Ship is out of fuel!", fill="white")
            canvas.create_rectangle((wW / 2) - 50, (wH / 2) + 10, (wW / 2) + 50, (wH / 2) + 50, fill="grey")
            canvas.create_text(wW / 2, (wH / 2) + 30, text="Restart", fill="white", anchor="center")

        # Dautt fall(bara svo að þegar þú ert dauður getur ekki haldið áfram)
        def dead(key):
            pass

        # Þegar þú deyrð
        def destroy(boom):
            global canvas
            global listi
            global sol
            global wW
            global wH
            canvas.create_circle(Sx, Sy, boom, fill="orange")
            for a in listi:
                canvas.delete(a)
            canvas.bind("<Key>", dead)
            user()
            canvas.create_text(wW / 2, wH / 2, text="Ship destroyed!", fill="white")
            canvas.create_rectangle((wW / 2) - 50, (wH / 2) + 10, (wW / 2) + 50, (wH / 2) + 50, fill="grey")
            canvas.create_text(wW / 2, (wH / 2) + 30, text="Restart", fill="white", anchor="center")

        def user():
            global wW
            global wH
            global e1
            e1 = Entry(canvas)
            canvas.create_text(wW / 2, (wH / 2) + 60, text="Sláðu inn notenda nafn þitt", fill="white")
            canvas.create_window(wW / 2, (wH / 2) + 80, window=e1)
        # Ef það er ýtt á músa takkann
        def callback(event):
            global canvas
            global dod
            global tel
            global e1
            canvas.focus_set()
            print("clicked at", event.x, event.y)
            if dod == True:
                if event.x > (wW / 2) - 50 and event.y > (wH / 2) + 10 and event.x < (wW / 2) + 50 and event.y < (wH / 2) + 50:
                    nafn = e1.get()
                    if nafn != "":
                        entry = ","+nafn+":"+str(tel)
                        with open("scores.txt","a") as f:
                            f.write(entry)
                    reset()

        # Til að búa til punkt
        def new_dot():
            global canvas
            global speed
            global dot
            global tel
            tel += 1
            global Dx
            global Dy
            global Dr
            global rooms
            global room
            global dtel

            Dx = random.randint(0, 1200)
            Dy = random.randint(0, 900)
            Dr = random.choice(rooms)
            tel1 = 0
            for a in range(628):
                if Dr == "R1":
                    print("Y:", Dy)
                    print("X:", Dx)
                    print("Ry:", round(900 + 300 * math.sin(tel)))
                    print("Rx:", round(1200 + 300 * math.cos(tel)))
                    if Dy > round(900 + 300 * math.sin(tel1)) and Dx > round(1200 + 300 * math.cos(tel1)):
                        print("yay!!")
                        new_dot()
                elif Dr == "R2":
                    if Dy > round(900 + 300 * math.sin(tel1)) and Dx < round(0 + 300 * math.cos(tel1)):
                        new_dot()
                elif Dr == "R3":
                    if Dy < round(0 + 300 * math.sin(tel1)) and Dx > round(1200 + 300 * math.cos(tel1)):
                        new_dot()
                elif Dr == "R4":
                    if Dy < round(0 + 300 * math.sin(tel1)) and Dx < round(0 + 300 * math.cos(tel1)):
                        new_dot()
                tel1 = round(tel1 + 0.01, 2)
                # print(tel)

        # Aðal skjár í geimskipi
        def homeSS():
            global canvas
            global dot
            global Cx
            global Cy
            global listi
            canvas.delete(dot)
            listi = []
            listi.append(canvas.create_circle(Cx, Cy, 50, fill="white", outline=""))

        # Aðal skjár í geimnum
        def homeS():
            global canvas
            global dot
            canvas.delete(dot)
            global Sx
            global Sy
            global listi
            listi = []
            global fY
            global room
            global Dr
            global dod
            global maxfuel
            global fuel
            global wW
            global wH
            if room == Dr:
                dot = canvas.create_circle(Dx, Dy, 3, fill="yellow")
            try:
                with open("scores.txt","r") as f:
                    text = f.read()
                    users = text.split(",")
                telja = 0
                for a in users:
                    nota = a.split(":")
                    if int(nota[1]) > int(telja):
                        nafn = nota[0]
                        telja = nota[1]
                listi.append(canvas.create_text(wW/2,0,text="Hæsti notandi: "+nafn+" : "+str(telja),fill ="white",anchor = N))
            except:
                listi.append(
                    canvas.create_text(wW / 2, 0, text="Hæsti notandi: Enginn", fill="white",anchor=N))
            if dod == False:
                if fY == "s":
                    listi.append(canvas.create_circle(Sx, Sy - 8, 3, fill="lightblue", outline=""))
                elif fY == "w":
                    listi.append(canvas.create_circle(Sx, Sy + 2, 3, fill="lightblue", outline=""))
                elif fY == "a":
                    listi.append(canvas.create_circle(Sx + 2, Sy, 3, fill="lightblue", outline=""))
                elif fY == "d":
                    listi.append(canvas.create_circle(Sx - 8, Sy, 3, fill="lightblue", outline=""))

                if fY == "s" or fY == "w":
                    listi.append(canvas.create_circle(Sx, Sy, 3, fill="grey", outline=""))
                    listi.append(canvas.create_circle(Sx, Sy - 2, 3, fill="grey", outline=""))
                    listi.append(canvas.create_circle(Sx, Sy - 4, 3, fill="grey", outline=""))
                    listi.append(canvas.create_circle(Sx, Sy - 6, 3, fill="grey", outline=""))
                elif fY == "a" or fY == "d":
                    listi.append(canvas.create_circle(Sx, Sy, 3, fill="grey", outline=""))
                    listi.append(canvas.create_circle(Sx - 2, Sy, 3, fill="grey", outline=""))
                    listi.append(canvas.create_circle(Sx - 4, Sy, 3, fill="grey", outline=""))
                    listi.append(canvas.create_circle(Sx - 6, Sy, 3, fill="grey", outline=""))
                if Sx - 3 <= Dx + 3 and Sx + 3 >= Dx - 3 and Sy - 3 <= Dy + 3 and Sy + 3 >= Dy - 3 and room == Dr:
                    fuel = fuel + 10
                    if fuel > maxfuel:
                        fuel = maxfuel
                    new_dot()
                if fuel == 0:
                    emty()
            listi.append(canvas.create_text(wW - 10, 10, text="Stig: " + str(tel), width=100, anchor=NE, fill="white"))
            listi.append(canvas.create_text(0 + 10, 10, text="Fuel: " + str(fuel), width=100, anchor=NW, fill="white"))

        # Til að búa til stjörnur
        def stars(numb, x1, y1, x2, y2):
            global canvas
            for a in range(numb):
                x = random.randint(x1, x2)
                y = random.randint(y1, y2)
                star.append(canvas.create_circle(x, y, 1, fill="white", outline=""))

        # Herbergi 1 í geimnum
        def R1():
            global canvas
            global dot
            global room
            room = "R1"
            canvas.delete(dot)
            for a in planets:
                canvas.delete(a)
            planets.append(canvas.create_circle(100, 120, 50, fill="blue", outline="lightblue", width=4))
            planets.append(canvas.create_circle_arc(100, 120, 48, fill="green", outline="", start=45, end=140))
            planets.append(canvas.create_circle_arc(100, 120, 48, fill="green", outline="", start=275, end=305))
            planets.append(canvas.create_circle_arc(100, 120, 45, style="arc", outline="white", width=6, start=270 - 25,
                                                    end=270 + 25))
            planets.append(canvas.create_circle(150, 40, 20, fill="#BBB", outline=""))
            planets.append(canvas.create_circle(140, 40, 2, fill="darkgrey", outline=""))
            planets.append(canvas.create_circle(160, 50, 4, fill="darkgrey", outline=""))
            planets.append(canvas.create_circle(160, 30, 3, fill="darkgrey", outline=""))

            planets.append(canvas.create_circle(1200, 900, 300, fill="#FF5C00"))
            planets.append(canvas.create_circle(1200, 900, 400, outline="#FF5C00"))

        # Herbergi 2 í geimnum
        def R2():
            global canvas
            global dot
            global room
            room = "R2"
            canvas.delete(dot)
            for a in planets:
                canvas.delete(a)
            planets.append(canvas.create_circle(0, 900, 300, fill="#FF5C00"))
            planets.append(canvas.create_circle(0, 900, 400, outline="#FF5C00"))

            planets.append(canvas.create_circle(900, 500, 45, fill="red"))
            planets.append(canvas.create_circle(880, 520, 10, fill="#E82A00", outline=""))
            planets.append(canvas.create_circle(920, 520, 8, fill="#E82A00", outline=""))
            planets.append(canvas.create_circle(900, 480, 5, fill="#E82A00", outline=""))

            planets.append(canvas.create_circle(500, 100, 60, fill="#FFA30B", outline="#FFBD05", width=4))

        # Herbergi 3 í geimnum
        def R3():
            global canvas
            global dot
            global room
            room = "R3"
            canvas.delete(dot)
            for a in planets:
                canvas.delete(a)
            planets.append(canvas.create_circle(1200, 0, 300, fill="#FF5C00"))
            planets.append(canvas.create_circle(1200, 0, 400, outline="#FF5C00"))

        # Herbergi 4 í geimnum
        def R4():
            global canvas
            global dot
            global room
            room = "R4"
            canvas.delete(dot)
            for a in planets:
                canvas.delete(a)
            planets.append(canvas.create_circle(0, 0, 300, fill="#FF5C00"))
            planets.append(canvas.create_circle(0, 0, 400, outline="#FF5C00"))

            planets.append(canvas.create_circle(900, 600, 150, fill="#FFA700"))
            planets.append(canvas.create_circle(900, 600, 225, outline="#FFE100", width=40))

        # Herbergi 1 í geimskipi
        def sR1():
            global canvas
            global dot
            global wW
            global wH
            global Seatx
            global Seaty
            global room
            room = "sR1"
            canvas.delete(dot)
            for a in planets:
                canvas.delete(a)
            planets.append(canvas.create_rectangle(0, 200, (wW / 4) * 3, 700, fill="darkgrey"))
            planets.append(canvas.create_polygon(900, 200, wW, wH / 2, 900, 700, fill="darkgrey"))
            planets.append(
                canvas.create_rectangle(Seatx - 50, Seaty - 50, Seatx + 50, Seaty + 50, fill="brown", outline=""))

        # Herbergi 2 í geimskipi
        def sR2():
            global canvas
            global wW
            global wH
            global room
            room = "sR2"
            for a in planets:
                canvas.delete(a)
            planets.append(canvas.create_rectangle(0, 200, wW, 700, fill="darkgrey"))

        # Herbergi 3 í geimskipi
        def sR3():
            global canvas
            global wW
            global wH
            global room
            room = "sR3"
            for a in planets:
                canvas.delete(a)
            planets.append(canvas.create_circle(300, wH / 2, 250, fill="lightblue", outline=""))
            planets.append(canvas.create_rectangle(300, 200, wW, 700, fill="darkgrey", outline=""))


        root = Tk()
        reset()
        root.mainloop()
    #Fall sem heldur utan um skæri, blað, steinn
    def sbs():
        global tel1
        global tel2
        global tel3
        tel1 = 0
        tel2 = 0
        tel3 = 0
        for a in root.winfo_children():
            a.destroy()
        #Fall fyrir ef það er valið skæri
        def skaeri():
            global tel1
            global tel2
            global tel3
            tala = random.randint(1, 3)
            if tala == 1:
                labelU.configure(text="Notandi: Skæri")
                labelT.configure(text="Tölva: Skæri")
                labelV.configure(text="Jafntefli")
                tel3 = tel3 + 1
                labelTj.configure(text=tel3)
            elif tala == 2:
                labelU.configure(text="Notandi: Skæri")
                labelT.configure(text="Tölva: Blað")
                labelV.configure(text="Notandi vinnur")
                tel1 = tel1 + 1
                labelTv.configure(text=tel1)

            else:
                labelU.configure(text="Notandi: Skæri")
                labelT.configure(text="Tölva: Steinn")
                labelV.configure(text="Tölva Vinnur")
                tel2 = tel2 + 1
                labelTt.configure(text=tel2)
        #Fall fyrir ef það er valið blað
        def blad():
            global tel1
            global tel2
            global tel3
            tala = random.randint(1, 3)
            if tala == 1:
                labelU.configure(text="Notandi: Blað")
                labelT.configure(text="Tölva: Skæri")
                labelV.configure(text="Tölva Vinnur")
                tel2 = tel2 + 1
                labelTt.configure(text=tel2)
            elif tala == 2:
                labelU.configure(text="Notandi: Blað")
                labelT.configure(text="Tölva: Blað")
                labelV.configure(text="Jafntefli")
                tel3 = tel3 + 1
                labelTj.configure(text=tel3)
            else:
                labelU.configure(text="Notandi: Blað")
                labelT.configure(text="Tölva: Steinn")
                labelV.configure(text="Notandi vinnur")
                tel1 = tel1 + 1
                labelTv.configure(text=tel1)
        #Fall fyrir ef það er valið stein
        def steinn():
            global tel1
            global tel2
            global tel3
            tala = random.randint(1, 3)
            if tala == 1:
                labelU.configure(text="Notandi: Steinn")
                labelT.configure(text="Tölva: Skæri")
                labelV.configure(text="Notandi vinnur")
                tel1 = tel1 + 1
                labelTv.configure(text=tel1)
            elif tala == 2:
                labelU.configure(text="Notandi: Steinn")
                labelT.configure(text="Tölva: Blað")
                labelV.configure(text="Tölva vinnur")
                tel2 = tel2 + 1
                labelTt.configure(text=tel2)
            else:
                labelU.configure(text="Notandi: Steinn")
                labelT.configure(text="Tölva: Blað")
                labelV.configure(text="Jafntefli")
                tel3 = tel3 + 1
                labelTj.configure(text=tel3)

        button_1 = Button(root, text="Skæri", command=skaeri)
        button_2 = Button(root, text="Blað", command=blad)
        button_3 = Button(root, text="Steinn", command=steinn)
        button_4 = Button(root, text="Til baka", command=leikir)

        labelU = Label(root, text="")
        labelT = Label(root, text="")
        labelV = Label(root, text="")

        labelTtxt = Label(root, text="Sigrar:")
        labelUtxt = Label(root, text="Töp:")
        labelVtxt = Label(root, text="Jafntefli:")

        labelTv = Label(root, text=tel1)
        labelTt = Label(root, text=tel2)
        labelTj = Label(root, text=tel3)

        button_1.grid(row=1, column=1)
        button_2.grid(row=2, column=1)
        button_3.grid(row=3, column=1)
        button_4.grid(columnspan=5)

        labelU.grid(row=1, column=2)
        labelT.grid(row=2, column=2)
        labelV.grid(row=3, column=2)

        labelTtxt.grid(row=1, column=3)
        labelUtxt.grid(row=2, column=3)
        labelVtxt.grid(row=3, column=3)

        labelTv.grid(row = 1, column = 4)
        labelTt.grid(row=2, column=4)
        labelTj.grid(row=3, column=4)

    label_1 = Label(root, text="Veldu hvað þú vilt gera")
    button_1 = Button(root, text=" Skæri, blað, steinn ", command=sbs)
    button_2 = Button(root, text=" Mylla ", command=mylla)
    button_3 = Button(root, text=" Planets ", command=Planets)
    button_4 = Button(root, text=" Til baka ", command=home)

    button_1.grid(row=1, column=1)
    button_2.grid(row=1, column=2)
    button_3.grid(row=1, column=3)
    button_4.grid(row=1, column=4)
    label_1.grid(columnspan=5)

#Bý til glugga
root = Tk()
#Byrti heimamynd
home()
#Læt gluggan keyra í loopu
root.mainloop()
