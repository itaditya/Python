#!/usr/bin/env python
import Tkinter as tk
top = tk.Tk()
quit = tk.Button(top, text='Close Me', command=top.quit)
quit.pack()
label = tk.Label(top, text='Hello World!')
label.pack()
tk.mainloop()
