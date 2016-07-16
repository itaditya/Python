#!/usr/bin/env python3
import  tkinter
top=tkinter.Tk()
quit=tkinter.Button(top,text='Close Me',command=top.quit)
quit.pack()
label=tkinter.Label(top,text='Hello World!')
label.pack()

# r =tkinter.Tk()
# r.withdraw()
# r.clipboard_clear()
# r.clipboard_append('Aditya is copied to clipboard')
# r.update()
# r.destroy()

r =tkinter.Tk()
text = r.clipboard_get()
r.withdraw()
r.update()
r.destroy()
label=tkinter.Label(top,text=text)
label.pack()


entry=tkinter.Entry(top)
entry.pack()
tkinter.mainloop()
