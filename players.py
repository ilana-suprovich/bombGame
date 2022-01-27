from tkinter import *

import sqlite3

con = sqlite3.connect('players.db')
cur = con.cursor()


class Players(Toplevel):

    # def add_person(self):
    #     add_page = AddPlayer()
    #     self.destroy()

    # def display_person(self):
    #     selected_item = self.listbox.curselection()
    #     if selected_item:
    #         person = self.listbox.get(selected_item)
    #         player_login = person.split(" ")
    #         display_page = Display(player_login)
    #     else:
    #         messagebox.showwarning("Error", "Empty cell. Choose someone.")

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("400x500")
        self.title("Your playing history")
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='black')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='white')
        self.bottom.pack(fill=X)

        self.heading = Label(self.top, text='Progress', font='arial 15 bold', bg='white', fg='black')
        self.heading.place(x=150, y=50)

        self.scrollbar = Scrollbar(self.bottom, orient=VERTICAL)

        self.listbox = Listbox(self.bottom, width=40, height=27)
        self.listbox.grid(row=0, column=0, padx=(40, 0))
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        players = cur.execute("select * from 'players'").fetchall()
        count = 0
        position = 1
        for player in players:
            self.listbox.insert(count, str(position) + "        " + str(player[0]) + "      " + str(player[1]))
            count += 1
            position += 1

        self.scrollbar.grid(row=0, column=1, sticky=N + S)

        # btn_add = Button(self.bottom, text='Add', width=12, font='Sans 12 bold', command=self.add_person)
        # btn_add.grid(row=0, column=2, padx=20, pady=10, sticky=N)
        #
        # btn_display = Button(self.bottom, text='Display', width=12, font='Sans 12 bold', command=self.display_person)
        # btn_display.grid(row=0, column=2, padx=20, pady=50, sticky=N)
