#!/usr/bin/env python3.4
import os

# Functions ---->

def html_src():
  src_file=open("src/markup.txt","r")
  html=src_file.read();
  src_file.close()
  return html

def css_src():
  src_file=open("src/css.txt","r")
  css=src_file.read();
  src_file.close()
  return css

def loc():
  root=input("Enter Project Location : ")
  return root

#Global Variables  ----->

html = html_src()
css = css_src()
# root = loc()

# -----------------------

def basic_setup():
  cmds = [
            "mkdir ../project",
            "mkdir ../project/css ../project/js ../project/assets" ,
            "touch ../project/index.html" ,
            "touch ../project/css/style.css" ,
            "touch ../project/js/main.js"
  ]
  execute(cmds)

def execute(cmds):
  for cmd in cmds:
    os.system(cmd)

def basic_html():
  file=open("../project/index.html","a")
  file.write(html)
  file.close()

def basic_css():
  file=open("../project/css/style.css","a")
  file.write(css)
  file.close()

def start():
  basic_setup()
  basic_html()
  basic_css()

start()
