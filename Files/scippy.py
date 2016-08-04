#!/usr/bin/env python3.4
# import random
import os

#Global Variables  ----->
html="" 
css=""
root=""
branch=""

# Functions ---->

def basic_setup():
  cmds = [
            "mkdir css js assets" ,
            "touch index.html" ,
            "touch css/style.css" ,
            "touch js/main.js"
  ]
  execute(cmds)
def execute(cmds):
  for cmd in cmds:
    print(cmd)
    os.system(cmd)
def basic_html():
  branch=root+"index.html"
  file=open(branch,"a")
  file.write(html)
  file.close()

def basic_css():
  file=open("css/style.css","a")
  file.write(html)
  file.close()

def html_src():
  src_file=open("src/markup.txt","r")
  html=src_file.read();
  src_file.close()

def css_src():
  src_file=open("src/css.txt","r")
  css=src_file.read();
  src_file.close()

def load_src():
  html_src()
  css_src()
  print(html+css)

def loc():
  root=input("Enter Project Location : ")
  # os.system("cd ~")
  cmd=" mkdir "+root+"/"
  os.system(cmd)
  cmd=" cd "+root
  os.system(cmd)


def start():
  loc()
  basic_setup()
  basic_html()
  basic_css()

load_src()
start()



