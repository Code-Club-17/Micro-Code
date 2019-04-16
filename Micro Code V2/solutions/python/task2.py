#!/usr/bin/env python3
#this for task2 
#here in text you can input any letter(abd...,ABC....) or number(012....) or symbol(@&"().....) like 
#


import string as str

letters=str.ascii_lowercase*2+str.ascii_uppercase*2+str.digits+str.punctuation+" " 
num=int(input())
_let=letters[num:-43]+letters[0:num]+letters[-43:]
text=input()
res=""

for _index,_char in enumerate(text):
  items=text.replace(_char,_let[letters.index(_char)])
  res=res+items
print(res[::len(text)+1])
