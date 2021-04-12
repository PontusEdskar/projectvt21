#!/usr/bin/env python
# coding: utf-8

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def devide(x, y):
    return x / y


print("Välj Räknesätt")
print("1.addera")
print("2.subbtrahera")
print("3.multiplicera")
print("4.dividera")

choice = input("Välj räknesätt(1/2/3/4): ")
if choice in ('1' , '2' , '3' , '4'):
    number1 = float(input("Det första nummret: "))
    number2 = float(input("Det andra nummret: "))
    x=number1
    y=number2
    
    if choice == '1':
        print (number1, "+", number2, "=", add(x, y))
        
    elif choice == '2':
        print(number1, "-", number2, "=", subtract(x, y))
        
    elif choice == '3':
        print(number1, "*", number2, "=", multiply(x, y))
        
    elif choice == '4':
        print(number1, "/", number2, "=", devide(x, y))
        
else:
    print("error")