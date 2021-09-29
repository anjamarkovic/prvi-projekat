"""". Napisati kod koji za datu godinu odreñuje da li je prestupna i štampa odgovarajuću
poruku. 
"""
godina= int(input("Unesite zeljenu godinu"))
if godina%400==0 :
    print("Godina je prestupna")
elif godina%100 != 0 and godina%4==0 :
    print("Godina je prestupna")
else:
    print("Godina nije prestupna")