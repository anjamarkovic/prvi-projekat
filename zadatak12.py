"""Dat je četvorocifreni prirodan broj abcd . Štampati poruku „Super“ ako važi a  c = b  d ."""
n= int(input("Unesite cetvorocifren broj n"))
b=(n//100)%10
c=(n//10)%10
if b==c :
    print("Super")