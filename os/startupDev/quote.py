#!/usr/bin/env python
import json
import requests
import Tkinter as tk

j = json.loads(requests.get(
    "http://quotes.stormconsultancy.co.uk/random.json").text)
top = tk.Tk()
top.configure(background="#300A24")
quit = tk.Button(top, text="Close Me", bg="#fff", padx=50,
                 fg="#555", borderwidth=0, command=top.quit)
quit.pack()
quote = tk.Label(top, text=j["quote"], height=10,
                 width=30, wraplength=300, bg="#300A24", padx=10, fg="#fff", font=("Helvetica", 14))
quote.pack()
author = tk.Label(top, text="-" + j["author"], anchor="e",
                  justify="right", padx=20, pady=15, bg="#300A24", fg="#fff", font=("Helvetica", 12))
author.pack()
# author.pack(side="right")

quit1 = tk.Button(top, text="Close Me", bg="#fff",
                  fg="#555", borderwidth=0, command=top.quit)
quit1.pack(side="left")
quit2 = tk.Button(top, text="Close Me", bg="#fff",
                  fg="#555", borderwidth=0, command=top.quit)
quit2.pack()
quit3 = tk.Button(top, text="Close Me", bg="#fff",
                  fg="#555", borderwidth=0, command=top.quit)
quit3.pack(side="right")
tk.mainloop()
