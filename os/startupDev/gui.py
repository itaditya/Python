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
        self.project = [{"name":"Portfolio","location": "F:\git\portfolio","command": "http://localhost:8080"},{"name":"JStack","location":"F:\git\JStack" ,"command": "http://localhost:8080"},{"name":"GPS_Track","location": "F:\git\GPS_Track","command": "http://localhost:8080"}]
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
        projectButton = Button(self, text=self.project[0]["name"],
                          style="Medium.TButton", command=lambda: self.btnFn(0))
        projectButton.pack(side=RIGHT)
        projectButton = Button(self, text=self.project[1]["name"],
                          style="Medium.TButton", command=lambda: self.btnFn(1))
        projectButton.pack(side=RIGHT)
        projectButton = Button(self, text=self.project[2]["name"],
                          style="Medium.TButton", command=lambda: self.btnFn(2))
        projectButton.pack(side=RIGHT)

    def getQuote(self):
        # j = json.loads(requests.get(
            # "http://quotes.stormconsultancy.co.uk/random.json").text)
        # self.quote = j["quote"]
        # self.author = j["author"]
        self.initUI()

    def btnFn(self,index):
        subprocess.Popen(
            ['explorer', self.project[index]["location"]])
        subprocess.Popen(
            ['subl', self.project[index]["location"]])
        subprocess.Popen(
            ['console'], cwd=self.project[index]["location"])
        subprocess.Popen(
            ['chrome', self.project[index]["command"]])


def main():

    root = Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
