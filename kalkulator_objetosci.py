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

def dodaj_powtorzenia_zmiesz_ciezar(c, powtorzenia, serie, skok, objetosc):
    for i in range(0, 5):
        j = 0
        p = powtorzenia
        for j in range(0, 5):
            if licz_objetosc(c, p, serie) >= proc_minus_obj and licz_objetosc(c, p, serie) <= proc_plus_obj: 
                wyswietl(c, p, serie, licz_objetosc(c, p, serie))
            p+=1
        if licz_objetosc(c, p, serie) >= proc_minus_obj and licz_objetosc(c, p, serie) <= proc_plus_obj:
            wyswietl(c, p, serie, licz_objetosc(c, p, serie))
        c-=float(skok)   

def zmniejsz_powtorzenia_dodaj_ciezar(ciezar, p, serie, skok, objetosc):
    for i in range(0, 5):
        j = 0
        c = ciezar
        for j in range(0, 7):
            if licz_objetosc(c, p, serie) >= proc_minus_obj and licz_objetosc(c, p, serie) <= proc_plus_obj: 
                wyswietl(c, p, serie, licz_objetosc(c, p, serie))
            c+=float(skok)             
        if licz_objetosc(c, p, serie) >= proc_minus_obj and licz_objetosc(c, p, serie) <= proc_plus_obj:
            wyswietl(c, p, serie, licz_objetosc(c, p, serie))
        p-=1

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

procent_plus = float(objetosc * 8 / 100)
procent_minus = float(objetosc * 3 / 100)
proc_plus_obj = float(objetosc) + float(procent_plus)
proc_minus_obj = float(objetosc) - float(procent_minus)

print('\nwiece powtorzen dla 1.25 przy objętosci {0}:'.format(objetosc))
dodaj_powtorzenia_zmiesz_ciezar(c, p, serie, 1.25, objetosc)
print('\nwiecej powtorzen dla 2.5 przy objętosci {0}:'.format(objetosc))
dodaj_powtorzenia_zmiesz_ciezar(c, p, serie, 2.5, objetosc)
print('\nmniej powtorzen dla 1.25 przy objętosci {0}:'.format(objetosc))
zmniejsz_powtorzenia_dodaj_ciezar(c, p, serie, 1.25, objetosc)
print('\nmniej powtorzen dla 2.5 przy objętosci {0}:'.format(objetosc))
zmniejsz_powtorzenia_dodaj_ciezar(c, p, serie, 2.5, objetosc)

