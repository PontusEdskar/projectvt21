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

def powerOf(x,y):
    return x**y  #definition för alla räknesätt som ska användas

manual = input("för manualen skriv 1, för kalkylatorn skriv 2: ")
if manual in ('1', '2'):
    if manual == '1':
        print("Först kommer det fram de räknesätten som användaren kan välja mellan. När användaren sedan har valt räknesättet får den skriva in två tal som programmet räknar ut beroende på räknesättet som tidigare valts")
    elif manual == '2':
        print("Välj Räknesätt")
        print("1.addera")
        print("2.subbtrahera")
        print("3.multiplicera")
        print("4.dividera")
        print("5.upphöjt")  #skriver upp vilka räknesätt som användaren kan välja mellan

        choice = input("Välj räknesätt(1/2/3/4/5): ")   #användaren väljer räknesättet som den vill använda
        if choice in ('1' , '2' , '3' , '4', '5'):
            number1 = float(input("Det första nummret: "))   #användaren skriver upp det första nummret
            number2 = float(input("Det andra nummret: "))    #användaren skriver upp det andra nummret
            x=number1        #gör så variabeln x och number1 blir samma sak
            y=number2        #gör så variabeln y och number2 blir samma sak
    
            if choice == '1':
                print (number1, "+", number2, "=", add(x, y))       #om användaren väljer addition så används detta
        
            elif choice == '2':
                print(number1, "-", number2, "=", subtract(x, y))     #vid subtraktion används denna kod
        
            elif choice == '3':
                print(number1, "*", number2, "=", multiply(x, y))     #om det är multiplikation som väljs så är det denna kod
        
            elif choice == '4':
                print(number1, "/", number2, "=", devide(x,y))     #vid division är det den här koden
        
            elif choice == '5':
                print(number1, "**", number2, "=", powerOf(x,y))     # om användaren väler upphöjt i är det den här koden som används
        
            else:
                print("ogiltigt räknesätt")     #om räknesättet är något annat än 1-5 skrivs detta ut