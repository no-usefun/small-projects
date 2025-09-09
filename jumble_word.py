 ### importing packages for the gam
import tkinter
from tkinter import *
import random
from tkinter import messagebox

### words for the game:-
    ## words to be displayed:-
word = ["IDNAI","TRAILASAU","GROOKNAA","ALETPBHA","NISATRIZE","AGO","OTFBOLAL","PILLOPOL","TYNOPH","CANADAON",
        "DETNAWNU","prrtoai","PAJAN","EROPASING","ACFIRA","GENTARINA","ENW KYOR","IOCMXE","JAPBUN","JARTGAU",
        "ANRSTAJAH","PLTRGOAU","ENIHCAM","ICIMDNEE","PGRPRHHOTOEA","HPOEEADHNS","ARI ECTIODINNOR","ORDAI TROCLNO",
        "MAICATTHMES","PLISCHOSYTOG","ARCTICTANA","IPCIACF NOACE","TWSE BGLAEN","ACTUALLOCR","BUEL WAHEL","HOPNROMIEC"]
    ## answer for the words
answer = ["india","australia","kangaroo","alphabet","sanitizer","goa","football","lollipop","python","anaconda",
          "unwanted","airport","japan","singapore","africa","argentina","new york","mexico","punjab","gujarat",
          "rajasthan","portugal","machine","medicine","photographer","headphones","air conditioner","radio control",
          "mathematics","psychologist","antarctica","pacific ocean","west bengal","calculator","blue whale",
          "microphone"]
    ## arranging the words and answer into range:-
num = random.randrange(0, 36, 1)

### creating the window:-
win = tkinter.Tk()
win.geometry("250x350+500+150")
win.title("Jumble word")
win.configure(bg = "#FAC42F")
win.resizable(0, 0)

### defining functions for the game:-
    ## storing the variable:-
ans = StringVar()
score = IntVar()
score.set(0)
    ## def 0:-
def skip():
    global word, answer, num
    n = int(score.get())
    if n > 0:
        num = random.randrange(0, 36, 1)
        lbl1.config(text = word[num])
        ent1.delete(0, END)
        scr = (n - 1)
        score.set(scr)
    elif n == 0:
        messagebox.showerror("Error", "You can't skip this word.\nYour score is zero")
    else:
        score.set(0)
    ## def 1:-
def rst1():
    global word, answer, num
    num = random.randrange(0, 36, 1)
    lbl1.config(text = word[num])
    ent1.delete(0, END)
    ## def 2:-
def default():
    global word, answer, num
    lbl1.configure(text = word[num])
    ## def 3:-
def check_ans():
    global word, answer, num, score
    var = ent1.get()
    if var == answer[num]:
        rst1()
        n = int(score.get())
        scr = (n + 1)
        score.set(scr)
    else:
        ent1.delete(0, END)
        messagebox.showerror("WRONG","Your answer is incorrect \nYou have not followed the condition.".center(10))
    ## def 4:-
def rst():
    global score
    score.set(0)
    rst1()
    messagebox.showinfo("New Game", "Program successfully restarted")

### creating labels and buttons for the game:-
    ## Label
        # Label
lbl = Label(win,
             text="SCORE:",
             font=("Verdana", 12, "bold"),
             bg="#FAC42F",
             fg="#0A79DF")
lbl.place(x=10)
txt_lbl = Label(win,
                font=("Verdana", 12, "bold"),
                bg="#FAC42F",
                fg="#0A79DF",
                textvar = score)
txt_lbl.place(x=90)
        # Label 1
lbl1 = Label(win,
             text="Your Text Here",
             font=("Verdana", 16, "bold"),
             bg="#FAC42F",
             fg="#192A56")
lbl1.pack(padx=5, pady=30, ipady=5)
        # Label 2
lbl2 = Label(win,
             text="*Write in small caps.",
             font=("Verdana", 6, "bold"),
             bg="#FAC42F",
             fg="grey")
lbl2.place(x=70, y=136)
    ## entry
ent1 = Entry(win,
             font=("Arial", 16),
             width=12,
             bg="orange",
             fg="#30336B",
             textvar=ans)
ent1.pack(padx=20, pady=5)
    ## button
        # check button
btn1 = Button(win,
              text="Check",
              font=("Comic sans ms", 12, "bold"),
              width=12,
              bd=2,
              relief="sunken",
              bg="#DAE0E2",
              fg="#43BE31",
              command=check_ans)
btn1.pack(pady=15)
        # skip button
btn2 = Button(win,
              text="Skip",
              font=("Comic sans ms", 12, "bold"),
              width=12,
              bd=2,
              relief="sunken",
              bg="#DAE0E2",
              fg="#B83227",
              command=skip)
btn2.pack(pady=5)
        # reset button
btn3 = Button(win,
              text="New Game",
              font=("Comic sans ms", 12, "bold"),
              width=12,
              bd=2,
              relief="sunken",
              bg="#DAE0E2",
              fg="#2475B0",
              command=rst)
btn3.pack(pady=5)

### running the default function:-
default()

### ending of the window
win.mainloop()
