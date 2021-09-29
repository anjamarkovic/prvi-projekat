"""Napisati kod koji provjerava da li je zbir cifara datog trocifrenog broj dvocifren broj. """
x=int(input("Unesite trocifren broj x"))
p=x//100
s=(x//10)%10
z=x%10

zbir=p+s+z

if zbir>=10 and zbir<=99 :
    print("Zbir cifara trocifrenog broja jeste dvocifren broj")
else:
    print(print("Zbir cifara trocifrenog broja nije dvocifren broj"))