from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.title('Tic Tac Toe')

click = True
count = 0
winner = False


def if_winner():
    global winner
    winner = False

    if b1['text'] == "X" and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_buttons()

    elif b4['text'] == "X" and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_buttons()

    elif b7['text'] == "X" and b8['text'] == 'X' and b9['text'] == 'X':
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_buttons()

    elif b1['text'] == "X" and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_buttons()

    elif b2['text'] == "X" and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_buttons()

    elif b3['text'] == "X" and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_buttons()

    elif b1['text'] == "X" and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_buttons()

    elif b3['text'] == "X" and b5['text'] == 'X' and b7['text'] == 'X':
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_buttons()

    elif b1['text'] == "O" and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_buttons()

    elif b4['text'] == "O" and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_buttons()

    elif b7['text'] == "O" and b8['text'] == 'O' and b9['text'] == 'O':
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_buttons()

    elif b1['text'] == "O" and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_buttons()

    elif b2['text'] == "O" and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_buttons()

    elif b3['text'] == "O" and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_buttons()

    elif b1['text'] == "O" and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_buttons()

    elif b3['text'] == "O" and b5['text'] == 'O' and b7['text'] == 'O':
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        disable_buttons()


def b_click(b):
    global click, count

    if b['text'] == ' ' and click == True:
        b['text'] = 'X'
        click = False
        count += 1
        if_winner()
    elif b['text'] == ' ' and click == False:
        b['text'] = 'O'
        click = True
        count += 1
        if_winner()
    else:
        messagebox.showerror("Tic Tac Toe", "Please select a blank box")


def disable_buttons():
    b1.config(DISABLED)
    b2.config(DISABLED)
    b3.config(DISABLED)
    b4.config(DISABLED)
    b5.config(DISABLED)
    b6.config(DISABLED)
    b7.config(DISABLED)
    b8.config(DISABLED)
    b9.config(DISABLED)


def play():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global click, count
    click = True
    count = 0
    # Buttons
    b1 = Button(tk, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b1))
    b2 = Button(tk, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b2))
    b3 = Button(tk, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b3))

    b4 = Button(tk, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b4))
    b5 = Button(tk, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b5))
    b6 = Button(tk, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b6))

    b7 = Button(tk, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b7))
    b8 = Button(tk, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b8))
    b9 = Button(tk, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


game_menu = Menu(tk)
tk.config(menu=game_menu)

options_menu = Menu(game_menu, tearoff=False)
game_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Restart", command=play)

play()
tk.mainloop()
