"""Za prirodan broj k, štampati frazu „Na izletu smo ubrali k pecuraka“, gdje završetak riječi
„pečurka“ prilagodite broju k. Npr. 101 pecurku, 1204 pecurke, 506 pecuraka. """
k= int(input("Unesite broj ubranih pecurki"))
if k%10==1 :
    print("Na izletu smo ubrali " , k , " pecurku")
elif k%10==2 or k%10 ==3 or k%10==4:
    print("Na izletu smo ubrali " , k , "pecurke")
else:
    print("Na izletu smo ubrali " , k , "pecuraka")
