#!/usr/bin/env python3
#this for task1
#here in the text "input" you can input any letter(abd...,ABC....) or number(012....) or symbol(@&"().....)


import string as str

letters=str.ascii_lowercase*2+str.ascii_uppercase*2+str.digits+str.punctuation+" "  
_let=letters[3:-43]+letters[0:3]+letters[-43:] # here slicing letters or drop 3 letters  
text=input("please enter your text") # here the text you want to crypted
res=""

for _index,_char in enumerate(text):
  items=text.replace(_char,_let[letters.index(_char)])  # the result is "a"="a","A"="A"... etc
  res=res+items
print(res[::len(text)+1])
