""" Napisati kod koji za kvadratnu jednačinu ax2
+ bx + c =0 ispituje da li ima realna rješenja. """
a= float(input("Unesite broj a"))
b= float(input("Unesite broj b"))
c= float(input("Unesite broj c"))

D=b*b-4*a*c
if D>=0 :
    print("Jednacina ima realna resenja")
else:
    print("Jednacina nema realna resenja")
