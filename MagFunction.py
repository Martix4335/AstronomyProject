from math import log10


def diam_to_mag(d1, d2):
    fl = pow(d2 / d1, 2)
    print("Il flusso luminoso è: " + str(fl))
    mag_0 = 5 + 5 * log10(d1 / 5)
    mag_1 = mag_0 + 2.5 * log10(fl)
    print("La magnitudine è: " + str(mag_1))


def mag_to_diam(mag):
    a = pow(10, (mag - 5) / 5)
    d = a * 5
    print("Il diametro del telescopio deve essere di: " + str(d) + " mm")
