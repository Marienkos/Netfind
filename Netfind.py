# Importations
from tkinter import *
from tkinter import messagebox
import webbrowser
import os

# Window properties
main = Tk()
main.title("Netfind")
main.resizable(False, False)

# Chronology
def chronology():
    path = "./Chronology.txt"
    if os.path.exists(path) == True:
        file = open(path, "r")
        lines = file.read(1000)
        file.close()

        # Window properties
        main_crn = Tk()
        main_crn.title("Chronology")
        main_crn.resizable(False, False)

        # Objects
        scr = Scrollbar(main_crn)
        lst = Listbox(main_crn, yscrollcommand = scr.set)

        # Configuration
        scr.config(command = lst.yview)
        for line in lines.split("|"):
            lst.insert(END, line)

        # Appareance
        lst.pack(side = LEFT, fill = BOTH)
        scr.pack(side = RIGHT, fill = Y)

        # Execution
        main_crn.mainloop()

    else:
        messagebox.showinfo(title = "No way!", message = "You have\nno datas")

# Search
def search():
    brw = webbrowser.open
    v_qry = qry.get()
    file = open("./Chronology.txt", "a")
    wrt = file.write
    if v_ggl.get() == 1:
        brw("https://www.google.com/search?q=" + v_qry)
        wrt(v_qry + " - Google|")
    if v_wkp.get() == 1:
        brw("https://it.wikipedia.org/wiki/" + v_qry)
        wrt(v_qry + " - Wikipedia|")
    if v_qwt.get() == 1:
        brw("https://www.qwant.com/?q=" + v_qry)
        wrt(v_qry + " - Qwant|")
    if v_amz.get() == 1:
        brw("https://www.amazon.com/s?k=" + v_qry)
        wrt(v_qry + " - Amazon|")
    if v_twt.get() == 1:
        brw("https://twitter.com/search?q=" + v_qry)
        wrt(v_qry + " - Twitter|")
    if v_ytb.get() == 1:
        brw("https://www.youtube.com/results?search_query=" + v_qry)
        wrt(v_qry + " - Youtube|")
    file.close()

# Clear
def clear():
    if messagebox.askyesno(title = "Sure?", message = "You will clear\nall datas"):
        os.remove("./Chronology.txt")

# Variables
v_ggl = IntVar()
v_wkp = IntVar()
v_qwt = IntVar()
v_amz = IntVar()
v_twt = IntVar()
v_ytb = IntVar()

# Objects
qry = Entry(main)
ggl = Checkbutton(main, text = "Google", variable = v_ggl, onvalue = 1, offvalue = 0)
wkp = Checkbutton(main, text = "Wikipedia", variable = v_wkp, onvalue = 1, offvalue = 0)
qwt = Checkbutton(main, text = "Qwant", variable = v_qwt, onvalue = 1, offvalue = 0)
amz = Checkbutton(main, text = "Amazon", variable = v_amz, onvalue = 1, offvalue = 0)
twt = Checkbutton(main, text = "Twitter", variable = v_twt, onvalue = 1, offvalue = 0)
ytb = Checkbutton(main, text = "Youtube", variable = v_ytb, onvalue = 1, offvalue = 0)
crn = Button(main, text = "Chrono", command = chronology)
src = Button(main, text = "Search", command = search)
clr = Button(main, text = "Clear", command = clear)

# Appareance
qry.grid(row = 0, column = 0, columnspan = 3, sticky = "ew")
ggl.grid(row = 1, column = 0, sticky = "w")
wkp.grid(row = 1, column = 1, sticky = "w")
qwt.grid(row = 1, column = 2, sticky = "w")
amz.grid(row = 2, column = 0, sticky = "w")
twt.grid(row = 2, column = 1, sticky = "w")
ytb.grid(row = 2, column = 2, sticky = "w")
crn.grid(row = 3, column = 0, sticky = "ew")
src.grid(row = 3, column = 1, sticky = "ew")
clr.grid(row = 3, column = 2, sticky = "ew")

# Execution
main.mainloop()
