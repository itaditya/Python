from Tkinter import Tk, RIGHT, LEFT, BOTH, RAISED, CENTER
from ttk import Frame, Button, Style, Label
import json
import requests
import subprocess


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.quote = "I was supposed to be a cool quote . But then internet abandoned me !"
        self.author = "Aditya"
        self.getQuote()

    def initUI(self):

        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("alt")

        # Styling
        self.style.configure('.', font=('Helvetica', 12), background="#300A24")
        self.style.configure(
            "PW.TLabel", foreground="#fff", background="#300A24", padding=20, justify=CENTER, wraplength="350")
        self.style.configure(
            "Medium.TButton", foreground="#300A24", background="#fff", borderwidth=0, padding=8, font=('Helvetica', 9))
        # Styling Ends

        quoteLabel = Label(self, text=self.quote, style="PW.TLabel")
        quoteLabel.pack()
        authorLabel = Label(self, text=self.author, style="PW.TLabel")
        authorLabel.pack()

        self.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Close This",
                             style="Medium.TButton", command=self.parent.quit)
        closeButton.pack(side=RIGHT)
        okButton = Button(
            self, text="Portfolio", style="Medium.TButton", command=self.btnOneFn)
        okButton.pack(side=RIGHT)
        okButton = Button(self, text="JStack",
                          style="Medium.TButton", command=self.btnTwoFn)
        okButton.pack(side=RIGHT)
        okButton = Button(self, text="Python",
                          style="Medium.TButton", command=self.btnThreeFn)
        okButton.pack(side=RIGHT)

    def hello(self):
        print("Print Hello")

    def getQuote(self):
        # j = json.loads(requests.get(
            # "http://quotes.stormconsultancy.co.uk/random.json").text)
        # self.quote = j["quote"]
        # self.author = j["author"]
        self.initUI()

    def btnOneFn(self):
        subprocess.Popen(
            ['explorer', "F:\git\portfolio"])
        subprocess.Popen(
            ['subl', 'F:\git\portfolio'])
        subprocess.Popen(
            ['console ', '-t ', 'New Tab'], cwd='F:\git\portfolio')

    def btnTwoFn(self):
        subprocess.Popen(
            ['explorer', "F:\git\JStack"])
        subprocess.Popen(
            ['subl', 'F:\git\JStack'])
        subprocess.Popen(
            ['console'], cwd='F:\git\JStack')
        subprocess.Popen(
            ['chrome', 'http://localhost:8080'])

    def btnThreeFn(self):
        subprocess.Popen(
            ['explorer', "F:\git\ClubPortal\public"])
        subprocess.Popen(
            ['subl', 'F:\git\ClubPortal\public'])
        subprocess.Popen(
            ['console'], cwd="F:\git\ClubPortal\public")
        subprocess.Popen(
            ['chrome', 'http://localhost:8080'])
        # "F:\git\Python"


def main():

    root = Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
