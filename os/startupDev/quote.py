import json
import requests
import Tkinter as tk

j = json.loads(requests.get(
    "http://quotes.stormconsultancy.co.uk/random.json").text)
# print j["author"], j["quote"]
#!/usr/bin/env python
top = tk.Tk()
top.configure(background='#fff')
quit = tk.Button(top, text='Close Me', bg="#fafafa", command=top.quit)
quit.pack()
quote = tk.Label(top, text=j["quote"], height=10,
                 width=30, wraplength=300, bg="#fff", padx=10, fg="#333", font=("Helvetica", 14))
quote.pack()
author = tk.Label(top, text="-" + j["author"], anchor="e",
                  justify='right', padx=20, pady=15, bg="#fff", fg="#444", font=("Helvetica", 12))
author.pack(side="right")
tk.mainloop()
