text = input("Zadej text: ")

stop = False
while not stop:
    nahrazovane = input("Jake pismenko chces nahradit?: ")
    substitut = input(f"Za jake chces zvolene pismenko {nahrazovane} nahradit?: ")
    sifra = ""
    #text.replace(nahrazovane, substitut)
    for i in range(len(text)):
        if text[i] == nahrazovane:
            sifra += substitut
        else:
            sifra += text[i]
    print(sifra)
    text = sifra
    if input("Pokud chcete skoncit, napiste STOP: ") == "STOP":
        stop = True