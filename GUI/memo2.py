#!/usr/bin/env python3.4
import datetime
import tkinter

def getTime():
	now = datetime.datetime.now()
	return (now.strftime("%d-%m-%Y %H:%M"))

def addContent(file):
		tag=input("Add a memo tag\n")
		tag+="\n"
		file.write(tag)

		file.write(getTime()+"\n")

		note=input("Input a note  \n")
		note+="\n\n"
		file.write(note)

		print(tag+" has been added to file")

		if(input("to stop entering notes type \"quit\" otherwise press Enter\n")=="quit"):
		 return 0
		else :
			return addContent(file)

def showMemo():
  	file=open("Files/memo.txt","r")
  	top=tkinter.Tk()
  	quit=tkinter.Button(top,text='Close Me',command=top.quit,bg='orange',fg='white')
  	quit.pack(fill=tkinter.X,expand=1)
  	label=tkinter.Label(top,text=file.read(),bg='white')
  	label.pack(fill=tkinter.Y,expand=1)
  	tkinter.mainloop()
  	file.close()

file = ""
choice = int(input("Hello\nEnter Your Choice\n1::Read Memos\t2::Add Notes\n"))

try:
	if(choice == 1) :
		print("Accessing Memos ...")
		showMemo()

	elif(choice == 2) :
		print("Yeah! Add a Note .....")

		try:
		 file=open("Files/memo.txt","a")
		 addContent(file)  

		finally:
		 showMemo()
		 file.close()

	else :
		print("Yaar Only Two Choices Are there .....")

except (ValueError,TypeError):
	print("Error")