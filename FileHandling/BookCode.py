#!/usr/bin/env python3.4
with open("Files/BookCode.txt","a") as f:
 
 print("\n\n\n\n\n\n\n\n\n!!!!!!!!*******  Utility to Maintain a File having the Name of Author & Subject, Barcode of book_bank_books issued in your Name  ********!!!!!!!!\n To Enter Records follow the incoming INSTRUCTIONS")
 
 while True:
  f.write(input("\nYour Name\n")+"\n\n")
  for i in range(1,7):
    f.write("    Subject\tBarcode\tAuthor\n")
    f.write(str(i))
    f.write(".) "+input("\nEnter Name of Subject\n")+"\t"+input("Enter Barcode of Book\n")+"\t"+input("Enter Name of Author\n")+"\n")
  f.write("\n\n")
  if input("Type 'quit' to EXIT otherwise press Return key\n")=="quit":
     break
file=open("Files/BookCode.txt","r")
print("\n"+file.read())  
  
   
 
