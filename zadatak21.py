"""". Dato je 6 realnih promjenljivih a1, a2, b1, b2, c1, c2. Provjeriti da li postoji trougao čija su
tjemena A(a1,a2), B(b1, b2) i C(c1,c2) i ako postoji odrediti dužine njegovih visina.
Napomena: izračunati površinu trougla Heronovim obrascem i preko visine, pa ih
uporediti. """
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
s=(a+b+c)/2
p= math.sqrt(s*(s-a)*(s-b)*(s-c))

if p>0 :
    print("Postoji")
    ha=(2*p)/a
    hb=(2*p)/b
    hc=(2*p)/c
    print(ha,hb,hc)
