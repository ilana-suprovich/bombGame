import sqlite3
from tkinter import *

con = sqlite3.connect('players.db')
cur = con.cursor()


class Display(Toplevel):

    def __init__(self, player_login):
        Toplevel.__init__(self)

        self.geometry("650x550")
        self.title("Display")
        self.resizable(False, False)

        query = """SELECT * FROM 'players' WHERE player_login = '{}'""".format(player_login)
        result = cur.execute(query).fetchone()
        self.player_login = player_login
        player_login = result[0]

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#34baeb')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='images/people.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text="Player`s info", font='arial 15 bold', bg='white', fg='green')
        self.heading.place(x=270, y=50)

        # Login
        self.label_name = Label(self.bottom, text='Login', font='arial 15 bold', fg='white', bg='green')
        self.label_name.place(x=49, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, player_login)
        self.entry_name.config(state='disabled')
        self.entry_name.place(x=150, y=40)




