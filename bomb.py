from tkinter import *
import datetime
from players import Players


import sqlite3

bomb = 30
score = 0
press_return = True


def start(event):
    global press_return
    global bomb
    global score
    if not press_return:
        pass
    else:
        bomb = 30
        score = 0
        label.config(text='')
        update_bomb()
        update_score()
        update_display()
        press_return = False


def update_display():
    global bomb
    global score
    if bomb > 50:
        bomb_label.config(image=normal_photo)
    elif 0 < bomb <= 50:
        bomb_label.config(image=no_photo)
    else:
        bomb_label.config(image=bang_photo)
    fuse_label.config(text='Fuse: ' + str(bomb))
    points_label.config(text='Score: ' + str(score))
    fuse_label.after(100, update_display)


def update_bomb():
    global bomb
    if is_alive():
        bomb -= 1
        fuse_label.after(400, update_bomb)


def update_score():
    global score
    if is_alive():
        score += 5
        points_label.after(3000, update_score)
    else:
        print("Game is over!")

def click(event=None):
    global bomb
    if is_alive():
        bomb += 1


def is_alive():
    global bomb
    global score
    if bomb == 0:
        label.config(text='Bang! Bang! Bang!')
        return False
    else:
        return True


def save_score():
    if not is_alive():
        date = datetime.datetime.now()
        con = sqlite3.connect('players.db')
        cur = con.cursor()
        cur.execute('Insert into players (player_score, date) values (?, ?) ', (score, date.strftime("%b %d %Y %H:%M:%S")))
        con.commit()


def additional_fuse():
    global bomb
    global score
    if buy_fuse_button:
        score -= 2
        bomb += 20
        points_label.after(3000, update_score)


# def add_player():
#     add_player = AddPlayer()


def players():
    view = Players()


# def login():
#     print(score)
#     auth = Authentication()

root = Tk()

root.title('Bang Bang')
root.geometry('750x600')
root.resizable(False, False)

background_image = PhotoImage(
    file='img/comic-book-black-white-page-template-divided-by-lines-with-speech-bubbles_212216-272.png')
background_label = Label(image=background_image)
background_label.place(relwidth=1, relheight=1)

label = Label(root, text='Press <enter> to start the game', bg="black", fg='#ffffff', font=('Times', 16))
label.pack()

fuse_label = Label(root, text='Fuse: ' + str(bomb), bg="black", fg="green", font=('Times', 14))
fuse_label.pack()
points_label = Label(root, text='Points: ' + str(score), bg='#000000', fg='#ffffff', font=('Times', 14))
points_label.pack()

no_photo = PhotoImage(file='img/bomb_no.png')
normal_photo = PhotoImage(file='img/bomb_normal.png')
bang_photo = PhotoImage(file='img/pow.png')

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="black", width=700, height=650)
canvas.create_image(350, 200, image=no_photo)

bomb_label = Label(root, image=no_photo)
bomb_label.pack()

click_button = Button(root, text='Press <spacebar> to gain scores', bg='#000000', fg='#ffffff', width=25,
                      font=('Comic Sans MS', 14), command=click)
click_button.pack()

buy_fuse_button = Button(root, text='Buy 20 fuse here for 2 points', bg='#000000', fg='#ffffff', width=25,
                         font=('Comic Sans MS', 14), command=additional_fuse)
buy_fuse_button.pack()

addButton = Button(root, text='Save score', font=('Comic Sans MS', 14),
                   width=15, bg='#000000', fg='#ffffff', command=save_score)
addButton.place(x=570, y=250)

viewButton = Button(root, text='Your history', font=('Comic Sans MS', 14),
                    width=15, bg='#000000', fg='#ffffff', command=players)
viewButton.place(x=570, y=300)

# viewButton = Button(root, text='Log in', font=('Comic Sans MS', 14),
#                     width=15, bg='#000000', fg='#ffffff', command=login)
# viewButton.place(x=570, y=200)

root.bind('<Return>', start)
root.bind("<space>", click)

root.mainloop()
