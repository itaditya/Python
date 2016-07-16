#!/usr/bin/env python3.4
import tkinter
try:
 file=open("new.txt","a")
 while True:
  print("Hello")
  name=input("What is your Name?\n")
  name+="\t"
  file.write(name)
  br=input("What is your Branch\n")
  br+="\t"
  file.write(br)
  yr=input("What is your Adm. Year\n")
  yr+="\n"
  file.write(yr)
  print(name+br+yr+" has been added to file")
  if(input("to stop entering data input \"quit\" otherwise press Enter\n")=="quit"):
   break 
  file.close()
 file=open("new.txt","r")
 top=tkinter.Tk()
 quit=tkinter.Button(top,text='Close Me',command=top.quit,bg='orange',fg='white')
 quit.pack(fill=tkinter.X,expand=1)
 label=tkinter.Label(top,text=file.read())
 label.pack()
 tkinter.mainloop()
  
finally:
 file.close()

