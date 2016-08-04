#!/usr/bin/env python3.4
import tkinter

top=tkinter.Tk()

diction={
	"python":"python is a snake which bites" ,
	"window":"window is something which is transparent"
}
def initiategui():
	quit=tkinter.Button(top,text='Close Me',command=top.quit)
	quit.pack()
	label=tkinter.Label(top,text="Copy text to view it's meaning")
	label.pack()
	tkinter.mainloop()


def search(key):
	value = diction.get(key)
	if(value):
		print(value)
		return (value)
	else :
		return ("")

def catchClip():
	r =tkinter.Tk()
	text = r.clipboard_get()
	r.withdraw()
	r.update()
	r.destroy()
	return text 

def display(top,key,meaning):
	label=tkinter.Label(top,text=key)
	label.pack()
	meaning=tkinter.Label(top,text=meaning)
	meaning.pack()
	top.destroy()
	
	# start()

def start():
	# initiategui()
	key=catchClip()
	key_before = key
	if(len(key)):
		meaning=search(key)
		if(len(meaning)):
			display(top,key,meaning)
			
while True:
	start()
# print (search())