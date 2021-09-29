""". Data je meta sa 10 koncentričnih krugova sa centrom u koordinatnom početku i 3 tačke
A1(x1,y1), A2(x2,y2) i A3(x3,y3). Za pogodak u najmanji krug dobija se 10 bodova, za
svaki od sljedećih krugova po jedan bod manje a za pogadak van mete dobija se 0
bodova. Napisati program koji učitava koordinate tačaka A1, A2 i A3 i štampa ukupan broj
bodova koji donose pogoci u tačke A1, A2 i A3. Smatrati da pogodak u tačku na rastojanju
npr. 3 od centra nosi isti broj bodova kao i pogodak u tačku na rastojanju 3.5 od centra. """
import math
x1=float(input ("Unesite prvu koordinatu tacke A1"))
y1= float(input ("Unesite drugu koordinatu tacke A1"))
x2=float(input ("Unesite prvu koordinatu tacke A2"))
y2=float(input ("Unesite drugu koordinatu tacke A2"))
x3=float(input ("Unesite prvu koordinatu tacke A3"))
y3=float(input ("Unesite drugu koordinatu tacke A3"))
#rastojanje od pogodtka do tacke 0.0
r1= math.sqrt(x1*x1+y1*y1)
r2= math.sqrt(x2*x2+y2*y2)
r3= math.sqrt(x3*x3+y3*y3)
#trenutni bod rastojanja
bodr1= int(10-r1)
bodr2= int(10-r2)
bodr3= int(10-r3)
#print(bodr1) stampa pogodak koji je zaokruzen ako je 3.5 stampa kao 3
if bodr1<0 or bodr2<0 or bodr3<0:
    print("Pogodak je van mete, vas rezultat je 0")
else:
    print(bodr1+bodr2+bodr3)