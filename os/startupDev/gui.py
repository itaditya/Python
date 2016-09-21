#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, RIGHT, LEFT, BOTH, RAISED
from ttk import Frame, Button, Style, Label
import json
import requests


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("alt")
        self.style.configure(
            "PW.TLabel", foreground="#fff", background="#300A24")
        self.style.configure('.', font=('Helvetica', 12))

        # frame = Frame(self, relief=RAISED, borderwidth=1)
        # frame.pack(fill=BOTH, expand=True)
        # self.parent.configure(background="#300A24")
        # j = json.loads(requests.get(
        #     "http://quotes.stormconsultancy.co.uk/random.json").text)
        # quote = Label(self, text=j["quote"], height=10,
        #               width=30, wraplength=300, bg="#300A24", padx=10, fg="#fff", font=("Helvetica", 14))
        # quote.pack()
        # author = Label(self, text="-" + j["author"], anchor="e",
        #                justify="right", padx=20, pady=15, bg="#300A24", fg="#fff", font=("Helvetica", 12))
        # author.pack()
        quote = Label(self, text="Loremipsumdolorsitamet,consecteturadipisicingelit.Architectovelitvitaemodialiquamquasnamautemassumendaplaceatdolorveritatisdignissimos,ipsumsequisolutaeosisteaccusamus,rerumrepudiandaeadipisci.", style="PW.TLabel")
        quote.pack()

        self.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Close", command=self.parent.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=LEFT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=LEFT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=LEFT, padx=5, pady=5)


def main():

    root = Tk()
    root.geometry("400x200+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
