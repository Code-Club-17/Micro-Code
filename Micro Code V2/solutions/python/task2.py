#!/usr/bin/env python3
#this for task2 
#here in text you can input any letter(abd...,ABC....) or number(012....) or symbol(@&"().....) like 
#


import string as str

letters=str.ascii_lowercase*2+str.ascii_uppercase*2+str.digits+str.punctuation+" " 
num=int(input("please enter your number between 0 - 25)) 
_let=letters[num:-43]+letters[0:num]+letters[-43:]
text=input("please enter your text") # feel free to input any words you want
res=""

for _index,_char in enumerate(text):
  items=text.replace(_char,_let[letters.index(_char)]) #letters here is case sensitive
  res=res+items
print(res[::len(text)+1])
