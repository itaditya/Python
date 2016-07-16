#!/usr/bin/env python3.4
import random
import time
w_u=int(0)
w_c=int(0)
i_u=0
i_c=0
def result(i_u,i_c):
 global w_u,w_c
 mv=i_u*10+i_c
 if(mv==13 or mv==21 or mv==32):
  w_u=w_u+50
  return 1
 elif(i_u==i_c):
  return 0
 else:
  w_c=w_c+50
  return 2
def choice(ch):
 if (ch==1):
  return "\nROCK "
 elif (ch==2):
  return "\nPAPER "
 elif (ch==3):
  return "\nSCISSORS "
def show(i_u,i_c):
 print("\n\nYou chose "+choice(i_u))
 print("\nThe Computer chose\n1....."," ")
 time.sleep(1)
 print('2...')
 time.sleep(1)
 print('3.')
 time.sleep(0.5)
 print(choice(i_c)*4)
 if(result(i_u,i_c)==0):
  print("Oh.. It seems to be a tough tie")
 elif(result(i_u,i_c)==1):
  print("The computer kneels against you.. Bravo!")
 else:
  print("The computer mocks you at your stupendous choice....")

print("\n\nPlay the Ancient Pythonian Game :: Rock Paper Scissors \n\n Brought to you by CosmoGames\nEnter the no. according to your choice\n")
while True:
  i_user=int(input("\n1::Rock\n2::Paper\n3::Scissors\n4::Exit\n"))
  if(i_user==4):
   break;
  i_comp=random.randint(1,3)
  show(i_user,i_comp)
  print("\n\nThe Scores Are...\nYou::{0}\nComputer::{1}".format(w_u,w_c))
  

 
 
 
