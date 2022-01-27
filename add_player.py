from tkinter import *
from tkinter import messagebox

# from my_people import MyPeople

import sqlite3

con = sqlite3.connect('players.db')
cur = con.cursor()
print("Success")
log = ''


class AddPlayer(Toplevel):

    def add_player(self):
        player_login = self.entry_name.get()
        player_password = self.entry_password.get()

        cur.execute('SELECT player_login from players where player_login=?', (player_login,))
        con.commit()
        if not cur.fetchone():
            query = "INSERT INTO players (player_login, player_password) VALUES (?,?)"
            cur.execute(query, (player_login, player_password))
            con.commit()
            messagebox.showinfo("Success", "Player added")
            print(f"New person added!")
        else:
            messagebox.showinfo("This login already exists!")

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x450")
        self.title("Add new player")
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=300, bg='white')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='Add new player', font='arial 15 bold', bg='white', fg='green')
        self.heading.place(x=200, y=50)

        # Login
        self.label_name = Label(self.bottom, text='Login', font='arial 15 bold', fg='white', bg='black')
        self.label_name.place(x=49, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, '')
        self.entry_name.place(x=160, y=40)

        self.label_password = Label(self.bottom, text='Password', font='arial 15 bold', fg='white', bg='black')
        self.label_password.place(x=49, y=80)

        self.entry_password = Entry(self.bottom, width=30, bd=4)
        self.entry_password.insert(0, '')
        self.entry_password.place(x=160, y=80)

        button = Button(self.bottom, text='Add player', width=27, height=1, command=self.add_player)
        button.place(x=147, y=250)


class Authentication(Toplevel):

    def login(self):
        global log
        log = StringVar()
        log = self.entry_login.get()
        password = self.entry_password.get()
        cur.execute('SELECT * from players where player_login=? and player_password=?', (log, password))
        con.commit()
        if cur.fetchone():
            messagebox.showinfo(title=None, message="Login successful!")
        else:
            messagebox.showinfo(title=None, message="Wrong username or password!!!")

    def __init__(self):
        Toplevel.__init__(self)
        self.title("Log in")
        self.geometry("550x450")

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=300, bg='white')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='Log in here', font='arial 15 bold', bg='white', fg='green')
        self.heading.place(x=200, y=50)

        self.label_login = Label(self.bottom, text='Login', font='arial 15 bold', fg='white', bg='black')
        self.label_login.place(x=49, y=40)

        self.entry_login = Entry(self.bottom, width=30, bd=4)
        self.entry_login.insert(0, '')
        self.entry_login.place(x=160, y=40)

        self.label_password = Label(self.bottom, text='Password', font='arial 15 bold', fg='white', bg='black')
        self.label_password.place(x=49, y=80)

        self.entry_password = Entry(self.bottom, width=30, bd=4)
        self.entry_password.insert(0, '')
        self.entry_password.place(x=160, y=80)

        button = Button(self.bottom, text='Log in', width=27, height=1, command=self.login)
        button.place(x=147, y=250)


def get_log():
    return log
