"""Dat je četvorocifren broj. Odrediti broj koji se dobija zamjenom treće i druge cifre. Npr. od
5804 dobija se 5084. """
n= int(input("Unesite cetvorocifren broj n"))
a=n//1000
b=(n//100)%10
c=(n//10)%10
d=n%100
print(a,c,b,d)

