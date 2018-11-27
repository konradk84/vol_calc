def wyswietl(ciezar, powtorzenia, serie, objetosc):
    print('objetosc dla ciezaru {0}, przy ilosci powtorzen {1} w {2} seriach wynosi {3}'.format(ciezar, powtorzenia, serie, objetosc))

def licz_objetosc(ciezar, powtorzenia, serie):
    objetosc = float(ciezar)*float(powtorzenia)*int(serie)
    return objetosc

def ustaw_skok_ciezaru(ciezar):
    c = float(ciezar)
    if c > 24:
        skok = 2.5
    if c < 25 and c > 10:
        skok = 1.25
    return skok

def licz_warianty(c, p, serie, skok, objetosc):
    for i in range(0, 5):
        p+=1
        #print('c {0} i p {1}'.format(c, p))
        while( (licz_objetosc(c, p, serie) < proc_minus_obj) and (licz_objetosc(c, p, serie) < proc_plus_obj) ):
            p+=1
        c-=float(skok)    
        wyswietl(c, p, serie, licz_objetosc(c, p, serie))

print('podaj ciezar')
ciezar = input()
print('podaj ilosc powtorzen')
powtorzenia = input()
print('podaj ilosc serii')
serie = input()
#print('podaj skok ciezaru')
#skok = input()

objetosc = licz_objetosc(ciezar, powtorzenia, serie)
wyswietl(ciezar, powtorzenia, serie, objetosc)
#skok = ustaw_skok_ciezaru(ciezar)
#print('skok: ', skok)

c = float(ciezar)
p = int(powtorzenia)

procent_plus = float(objetosc * 5 / 100)
procent_minus = float(objetosc * 3 / 100)
proc_plus_obj = float(objetosc) + float(procent_plus)
proc_minus_obj = float(objetosc) - float(procent_minus)

print('\ndla 1.25:')
licz_warianty(c, p, serie, 1.25, objetosc)
print('\ndla 2.5:')
licz_warianty(c, p, serie, 2.5, objetosc)

'''
    obj = licz_objetosc(c, p, serie)
    if (float(obj) + skok) < float(objetosc):
        p+=1
        obj2 = licz_objetosc(c, p, serie)
        if float(obj2) > float(obj) and float(obj2) < float(objetosc):
            print('obj2: ', obj2)
        else:
            print('obj: ', obj) 
'''