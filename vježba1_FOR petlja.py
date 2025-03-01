pocetna_pozicija = 0
cilj = 50
trenutna_pozicija = 0
brzina = 10

for x in range (10):    #10 kretanja brzine, gdje pratimo poziciju automobila u odnosu na poziciju
    print(trenutna_pozicija)
    if trenutna_pozicija == cilj:
        print("Stigao do cilja")
        break   #koristi se za izlaz iz petlje nakon linije nakon koje želimo da izadjemo
    elif trenutna_pozicija > cilj:
        print ("Prošli ste cilj")
    elif trenutna_pozicija < cilj:
        print("Niste još stigli")
    trenutna_pozicija += brzina