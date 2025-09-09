### importing packages for the code:-
from tkinter import messagebox
from tkinter import *


### creating the screen:-
win = Tk()
win.title("TIC TAC TOE GAME".title())
win.configure(background = "Powder Blue")
win.resizable(0, 0)


### different frames of the screen:-
## frame 1
frm1 = Frame(win, bd=5, bg = "Blue", pady=2, width= 400, height=400, relief="ridge")
frm1.grid(row=0, column=0)
## frame 2
frm2 = Frame(win, bd=5, bg ="#A0EFEF", width= 400, height=300, relief="ridge")
frm2.grid(row=0, column=1)
# top
frm2_1 = Frame(frm2, bg = "#A0AFFF", padx=10, pady=2, width= 350, height=130, bd= 5, relief="groove")
frm2_1.grid(row=0, column=0)
# top 1
frm2_1_1 = Frame(frm2_1, bg = "#A0AFFF", padx=10, pady=2, width= 250, height=65, bd= 5, relief="groove")
frm2_1_1.grid(row=1, column=0)
# bottom
frm2_2 = Frame(frm2, bg = "#A0AFFF", padx=10, pady=2, width= 350, height=130, bd= 5, relief="groove")
frm2_2.grid(row=1, column=0)


### saving and defining game variable game variable:-
plr1 = IntVar()
plr1.set(0)
plr2 = IntVar()
plr2.set(0)
lbl = StringVar()
click = True
## function and rules:-
def checker(btns):
    global click
    if btns["text"] == " " and click == True:
        btns["text"] = "X"
        click = False
    elif btns["text"] == " " and click == False:
        btns["text"] = "O"
        click = True
    scorer()
## score :-
def scorer():
## for winning the game:-
    # for X
    if btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X":
        btn1.configure(background = "Blue")
        btn2.configure(background = "Blue")
        btn3.configure(background = "Blue")
        n = int(plr1.get())
        score = (n + 1)
        plr1.set(score)
        messagebox.showinfo("WON", "Player 1 has won the game")
        rst()
    elif btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X":
        btn4.configure(background = "orange")
        btn5.configure(background = "Orange")
        btn6.configure(background = "Orange")
        n = int(plr1.get())
        score = (n + 1)
        plr1.set(score)
        messagebox.showinfo("WON", "Player 1 has won the game")
        rst()
    elif btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X":
        btn7.configure(background = "green")
        btn8.configure(background = "green")
        btn9.configure(background = "green")
        n = int(plr1.get())
        score = (n + 1)
        plr1.set(score)
        messagebox.showinfo("WON", "Player 1 has won the game")
        rst()
    elif btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X":
        btn1.configure(background = "yellow")
        btn4.configure(background = "yellow")
        btn7.configure(background = "yellow")
        n = int(plr1.get())
        score = (n + 1)
        plr1.set(score)
        messagebox.showinfo("WON", "Player 1 has won the game")
        rst()
    elif btn2["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X":
        btn2.configure(background = "pink")
        btn5.configure(background = "pink")
        btn8.configure(background = "pink")
        n = int(plr1.get())
        score = (n + 1)
        plr1.set(score)
        messagebox.showinfo("WON", "Player 1 has won the game")
        rst()
    elif btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X":
        btn3.configure(background = "brown")
        btn6.configure(background = "brown")
        btn9.configure(background = "brown")
        n = int(plr1.get())
        score = (n + 1)
        plr1.set(score)
        messagebox.showinfo("WON", "Player 1 has won the game")
        rst()
    elif btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X":
        btn1.configure(background = "#ff0086")
        btn5.configure(background = "#ff0086")
        btn9.configure(background = "#ff0086")
        n = int(plr1.get())
        score = (n + 1)
        plr1.set(score)
        messagebox.showinfo("WON", "Player 1 has won the game")
        rst()
    elif btn3["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X":
        btn3.configure(background = "#f0a06f")
        btn5.configure(background = "#f0a06f")
        btn7.configure(background = "#f0a06f")
        n = int(plr1.get())
        score = (n + 1)
        plr1.set(score)
        messagebox.showinfo("WON", "Player 1 has won the game")
        rst()
    # for O
    elif btn1["text"]=="O" and btn2["text"]=="O" and btn3["text"]=="O":
        btn1.configure(background = "Blue")
        btn2.configure(background = "Blue")
        btn3.configure(background = "Blue")
        n = int(plr2.get())
        score = (n + 1)
        plr2.set(score)
        messagebox.showinfo("WON", "Player 2 has won the game")
        rst()
    elif btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O":
        btn4.configure(background = "orange")
        btn5.configure(background = "orange")
        btn6.configure(background = "orange")
        n = int(plr2.get())
        score = (n + 1)
        plr2.set(score)
        messagebox.showinfo("WON", "Player 2 has won the game")
        rst()
    elif btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O":
        btn7.configure(background = "green")
        btn8.configure(background = "green")
        btn9.configure(background = "green")
        n = int(plr2.get())
        score = (n + 1)
        plr2.set(score)
        messagebox.showinfo("WON", "Player 2 has won the game")
        rst()
    elif btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O":
        btn1.configure(background = "yellow")
        btn4.configure(background = "yellow")
        btn7.configure(background = "yellow")
        n = int(plr2.get())
        score = (n + 1)
        plr2.set(score)
        messagebox.showinfo("WON", "Player 2 has won the game")
        rst()
    elif btn2["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O":
        btn2.configure(background = "pink")
        btn5.configure(background = "pink")
        btn8.configure(background = "pink")
        n = int(plr2.get())
        score = (n + 1)
        plr2.set(score)
        messagebox.showinfo("WON", "Player 2 has won the game")
        rst()
    elif btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O":
        btn3.configure(background = "Brown")
        btn6.configure(background = "Brown")
        btn9.configure(background = "Brown")
        n = int(plr2.get())
        score = (n + 1)
        plr2.set(score)
        messagebox.showinfo("WON", "Player 2 has won the game")
        rst()
    elif btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O":
        btn1.configure(background = "#ff0086")
        btn5.configure(background = "#ff0086")
        btn9.configure(background = "#ff0086")
        n = int(plr2.get())
        score = (n + 1)
        plr2.set(score)
        messagebox.showinfo("WON", "Player 2 has won the game")
        rst()
    elif btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O":
        btn3.configure(background = "#f0a06f")
        btn5.configure(background = "#f0a06f")
        btn7.configure(background = "#f0a06f")
        n = int(plr2.get())
        score = (n + 1)
        plr2.set(score)
        messagebox.showinfo("WON", "Player 2 has won the game")
        rst()
## code to tie the game:-
    # for o
    elif btn1["text"]=="O" and btn3["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O" and btn8["text"]=="O":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn1["text"]=="O" and btn7["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O" and btn8["text"]=="O":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn2["text"]=="O" and btn3["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O" and btn9["text"]=="O":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn2["text"]=="O" and btn3["text"]=="O" and btn4["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn2["text"]=="O" and btn4["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O" and btn9["text"]=="O":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn2["text"]=="O" and btn4["text"]=="O" and btn6["text"]=="O" and btn7["text"]=="O" and btn9["text"]=="O":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn1["text"]=="O" and btn3["text"]=="O" and btn4["text"]=="O" and btn6["text"]=="O" and btn8["text"]=="O":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn1["text"]=="O" and btn3["text"]=="O" and btn4["text"]=="O" and btn9["text"]=="O" and btn8["text"]=="O":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn1["text"]=="O" and btn3["text"]=="O" and btn6["text"]=="O" and btn7["text"]=="O" and btn8["text"]=="O":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn1["text"]=="O" and btn2["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O" and btn7["text"]=="O":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn3["text"]=="O" and btn4["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O":
        messagebox.showinfo("Draw", "Game is draw")
    # for x
    elif btn2["text"]=="X" and btn3["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X" and btn9["text"]=="X":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn1["text"]=="X" and btn3["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" and btn8["text"]=="X":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn1["text"]=="X" and btn7["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" and btn8["text"]=="X":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn2["text"]=="X" and btn4["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X" and btn9["text"]=="X":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn2["text"]=="X" and btn4["text"]=="X" and btn6["text"]=="X" and btn7["text"]=="X" and btn9["text"]=="X":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn1["text"]=="X" and btn3["text"]=="X" and btn4["text"]=="X" and btn6["text"]=="X" and btn8["text"]=="X":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn1["text"]=="X" and btn3["text"]=="X" and btn6["text"]=="X" and btn7["text"]=="X" and btn8["text"]=="X":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn1["text"]=="X" and btn2["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" and btn7["text"]=="X":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn1["text"]=="X" and btn3["text"]=="X" and btn4["text"]=="X" and btn9["text"]=="X" and btn8["text"]=="X":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn2["text"]=="X" and btn3["text"]=="X" and btn4["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X":
        messagebox.showinfo("Draw", "Game is draw")
    elif btn3["text"]=="X" and btn4["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X":
        messagebox.showinfo("Draw", "Game is draw")
## reset button:-
def rst():
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "
    btn1.configure(background="#A0CFFF")
    btn2.configure(background="#A0CFFF")
    btn3.configure(background="#A0CFFF")
    btn4.configure(background="#A0CFFF")
    btn5.configure(background="#A0CFFF")
    btn6.configure(background="#A0CFFF")
    btn7.configure(background="#A0CFFF")
    btn8.configure(background="#A0CFFF")
    btn9.configure(background="#A0CFFF")
## new game button:-
def n_g():
    rst()
    plr1.set(0)
    plr2.set(0)
## exit quit code
def exit_():
    exit(0)

### creating buttons for the game:-
## for frame 2:-
# score
lbl3 = Label(frm2_1, font=("Times new roman", 22, "bold"), text="SCORE", fg="blue", bg = "#A0AFFF")
lbl3.grid(row=0, column=0)
# player1
lbl1 = Label(frm2_1_1, font=("arial", 16, "bold"), text="Player 1:", fg="red", bg = "#A0AFFF", padx=10, pady=2)
lbl1.grid(row=0, column=0, sticky= W)
txt_lab1 = Label(frm2_1_1, font=("arial", 16, "bold"), fg="#AFFFAF", bg = "#A0AFFF", textvar=plr1, width=5)
txt_lab1.grid(row=0, column=1)
# player2
lbl2 = Label(frm2_1_1, font=("arial", 16, "bold"), text="Player 2:", fg="red", bg = "#A0AFFF", padx=10, pady=2)
lbl2.grid(row=1, column=0, sticky= W)
txt_lab2 = Label(frm2_1_1, font=("arial", 16, "bold"), fg="#AFFFAF", bg = "#A0AFFF", textvar=plr2, width=5)
txt_lab2.grid(row=1, column=1)
# reset button
reset = Button(frm2_2, font="Times 22 bold", text="RESET".title(), width=12, bg = "#A0AFFF", fg="blue",
               bd=5, relief="sunken", command=rst)
reset.grid(row=0, column=0)
# new game button
new_game = Button(frm2_2, font="Times 22 bold", text="NEW GAME".title(), width=12, bg = "#A0AFFF", fg="blue",
                bd=5, relief="sunken", command=n_g)
new_game.grid(row=1, column=0)
# quit
quit = new_game = Button(frm2_2, font="Times 22 bold", text="Exit".title(), width=12, bg = "#A0AFFF", fg="blue",
                bd=5, relief="sunken", command=exit_)
new_game.grid(row=2, column=0)
## for frame 1:-
# button1
btn1 = Button(frm1, text=" ", bg = "#A0CFFF",font="Times 22 bold", height=4, width=8,
              command=lambda:checker(btn1))
btn1.grid(row=0, column=0, sticky= S+N+E+W)
# button2
btn2 = Button(frm1, text=" ", bg = "#A0CFFF",font="Times 22 bold", height=4, width=8,
              command=lambda:checker(btn2))
btn2.grid(row=0, column=1, sticky= S+N+E+W)
# button3
btn3 = Button(frm1, text=" ", bg = "#A0CFFF",font="Times 22 bold", height=4, width=8,
              command=lambda:checker(btn3))
btn3.grid(row=0, column=2, sticky= S+N+E+W)
# button4
btn4 = Button(frm1, text=" ", bg = "#A0CFFF",font="Times 22 bold", height=4, width=8,
              command=lambda:checker(btn4))
btn4.grid(row=1, column=0, sticky= S+N+E+W)
# button5
btn5 = Button(frm1, text=" ", bg = "#A0CFFF",font="Times 22 bold", height=4, width=8,
              command=lambda:checker(btn5))
btn5.grid(row=1, column=1, sticky= S+N+E+W)
# button6
btn6 = Button(frm1, text=" ", bg = "#A0CFFF", font="Times 22 bold", height=4, width=8,
              command=lambda:checker(btn6))
btn6.grid(row=1, column=2, sticky= S+N+E+W)
# button7
btn7 = Button(frm1, text=" ", bg = "#A0CFFF", font="Times 22 bold", height=4, width=8,
              command=lambda:checker(btn7))
btn7.grid(row=2, column=0, sticky= S+N+E+W)
# button8
btn8 = Button(frm1, text=" ", bg = "#A0CFFF", font="Times 22 bold", height=4, width=8,
              command=lambda:checker(btn8))
btn8.grid(row=2, column=1, sticky= S+N+E+W)
# button9
btn9 = Button(frm1, text=" ", bg = "#A0CFFF", font="Times 22 bold", height=4, width=8,
              command=lambda:checker(btn9))
btn9.grid(row=2, column=2, sticky= S+N+E+W)


### ending of the code:-
win.mainloop()
