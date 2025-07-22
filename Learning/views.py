from django.shortcuts import render
from django.http import HttpResponse
####

SumNumber=lambda Number1,Number2:Number1+Number2
PrintMessage= print (f"The number is:{SumNumber(20,40)}")
print (PrintMessage)

####
class FirstLastName:
    def __init__(self,name,nickname):
        self.name=name
        self.nickname=nickname
    def PrintString (self):
        print (f"My name is {self.name} {self.nickname}")
variable=FirstLastName ("Mahboubeh","Jalalifar")
variable.PrintString()

####
def average (Num1,Num2,Num3):
    ave=(Num1+Num2+Num3)//3
    return (f"The average score is:{ave}")
final=average (5,5,5)
print (final)

####
def exponent (Num4):
    exnum=(Num4)**2
    return (f"The Exponentiation is:{exnum}")
ex=exponent (5)
print (ex)

####     
class Even :
    number=0
    def even (self,x):
        self.number=x
        for char in range (0,x,2):
            print (char)
var=Even()
var.even(20)