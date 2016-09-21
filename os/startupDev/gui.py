#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, RIGHT, LEFT, BOTH, RAISED
from ttk import Frame, Button, Style


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

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
    # root.geometry("300x200+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
