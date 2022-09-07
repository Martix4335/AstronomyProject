from MagFunction import diam_to_mag
from MagFunction import mag_to_diam

while True:
    print("1) Calcola magnitudine")
    print("2) Calcola diametro")
    print("3) Esci")
    scelta = int(input("Scegli: "))
    if scelta == 1:
        d1 = float(input("Inserisci diametro lente: "))
        # while d1 is not float or not int:
        #    try:
        #        d1=float(d1)
        #        break
        #    except ValueError:
        #        print("Inserisci un numero")
        #        d1=(input("Inserisci diametro lente: "))
        d2 = float(input("Inserisci diametro lente: "))
        # while d2 is not float or not int:
        #    try:
        #        d2=float(d2)
        #    except ValueError:
        #        print("Inserisci un numero")
        #        d2=(input("Inserisci diametro lente: "))
        diam_to_mag(d1, d2)
    elif scelta == 2:
        mag = float(input("Inserisci la magnitudine: "))
        mag_to_diam(mag)
    elif scelta == 3:
        break
    else:
        print("Scelta non valida")
