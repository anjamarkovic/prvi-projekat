"""Dati su realni brojevi x, y,α, β, a i b. Napisati kod koji izračunava sljedeće izraze: """
import math
x= float(input("Unesite broj x"))
y= float(input("Unesite broj y"))
a= (x*x*x)/3 - 3*y*y + (x+1)/(2*y-3)
print(a)

import math
x= float(input("Unesite broj x"))
y= float(input("Unesite broj y"))
b= -5*(math.sqrt(x+math.sqrt(y)))
print(b)

import math
x= float(input("Unesite broj x"))
y= float(input("Unesite broj y"))
c= 1+1/(2+1/(3+0.75))
print(c)

import math
alfa= float(input("Unesite ugao alfa"))
beta= float(input("Unesite ugao beta"))
d=3 * math.sin(alfa)* 2 * math.cos(beta)- 5 * math.tan(alfa+beta) *  math.tan(alfa+beta)
print(d)

import math
a= float(input("Unesite broj a"))
b= float(input("Unesite broj b"))
alfa= float(input("Unesite ugao alfa"))
e= math.math.sqrt(a*a+b*b-2*a*a*b* math.sin(alfa))
print(e)
