symboly = ["x", "o"]

pole = [[0]*3 for i in range(3)]

while True:
    for ihrac in range(len(symboly)):
        pozice = int(input(f"Hraje hrac {ihrac+1} se symbolem {symboly[ihrac]}: "))
        radek, sloupec = (pozice-1)//3, (pozice-1)%3
        pole[radek][sloupec] = ihrac+1

        for radek in pole:
            print(radek)

        for iradek in range(3): #zbytecne
            vitezstvi = True
            for jsloupec in range(3):
                if pole[iradek][jsloupec] != ihrac+1:
                    vitezstvi = False
        if vitezstvi:
            print(f"hrac {ihrac+1} vyhral")