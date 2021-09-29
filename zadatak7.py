"""Napisati program koji učitava šest realnih brojeva x1, y1, x2, y2, x3, y3 koji redom
predstavljaju koordinate tačaka A(x1, y1), B(x2, y2) i C(x3, y3) i štampa površinu i obim
trougla ABC. """
import math
x1=float(input ("Unesite prvu koordinatu tacke A"))
y1= float(input ("Unesite drugu koordinatu tacke A"))
x2=float(input ("Unesite prvu koordinatu tacke B"))
y2=float(input ("Unesite drugu koordinatu tacke B"))
x3=float(input ("Unesite prvu koordinatu tacke C"))
y3=float(input ("Unesite drugu koordinatu tacke C"))
a= math.sqrt ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
b= math.sqrt ((x3-x2)*(x3-x2) + (y3-y2)*(y3-y2))
c= math.sqrt ((x3-x1)*(x3-x1) + (y3-y1)*(y3-y1))
o=a+b+c
s=(a+b+c)/2
p= math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Obim je:", o)
print("Povrsina je:", p)