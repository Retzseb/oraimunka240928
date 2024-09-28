def elso():

    print("A program eldönti egy egész számról, hogy pozitív-e""")
    szam = int(input("Kérem adjon meg egy egész számot!"))

    if szam > 0:
        print("A szám pozitív.")

def masodik():
    szam = int(input("Kérem adjon meg egy egész számot!"))

    if (szam>= -9) and (szam <=9):
        megelozo = szam - 1
        rakovetkezo = szam + 1
        print("A rákövetkez érték: "+str(rakovetkezo)+", a megelőző érték:"+str(megelozo))

