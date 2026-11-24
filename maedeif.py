# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:40:52 2026

@author: PC123
"""


#شرط ها
#ایف ینی اگر
age  = int(input("enter your age"))
if age <18: 
    print("salam bache") 
if age >=30 :   
    print("salam moosen")
    
age = 18
if age <18 :    
    print('salam bache')
if age >30:
    print("salam moosen")
#در غیر این صورت الیف میشه
sen =160
if sen <18 :
    print("salam baceh")
elif sen <40 :
    print("salam miansal")
else:
    print("bikhial")

#الس نباید جلوش نوشته بشه 
action ="gool"
socer =0 
if action == "shoot":
    print("oh shoot kard")
elif action == "pass" :
    print("pass dad be dostesh")
elif action == "gool":
    print("gooooooooool")
    socer+=1
else :
    print("chekardi")
if socer >0 :
    print(f" win {socer}")
number = int(input("enter your number"))
if number %2 ==0 :
    print("even")
else:
    print("odd")
