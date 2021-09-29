""". Dato je 6 realnih promjenljivih a1, a2, b1, b2, c1, c2. Odrediti da li je trougao čija su
tjemena A(a1,a2), B(b1,b2) i C(c1,c2) oštrougli, pravougli ili tupougli i štampati
odgovarajuću poruku (npr. „Ostrougli“). """
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


if math.sqrt(a * a + b * b)==c:
    print("Trougao je pravougli")
elif math.sqrt(a * a + b * b)>c :
    print("Trougao je ostrougli")
else:
     print("Trougao je tupougli")