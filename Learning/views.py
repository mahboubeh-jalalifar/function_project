from django.shortcuts import render
from django.http import HttpResponse
#SUM
def SumNumber (request):
    number1=10
    number2=20
    message=number1+number2
    return HttpResponse (f"The sum number is:{message}")
    
#NickName
def FirstLastName (request):
    name="Mahboubeh"
    lastname= "Jalalifar"
    return HttpResponse (f"My name is, {name} {lastname}")

#Average
def average (request):
    ave=(5+5+5)//3
    return HttpResponse (f"The average score is:{ave}")


#exponent
def exponent (request):
    exnum=4**2
    return HttpResponse (f"The Exponentiation is:{exnum}")

#even    
def even (request):
    n= 20
    message2=[str (char) for char in range (0,n,2)]
    n=n+1
    return HttpResponse (f"The even numbers is:{message2}")
