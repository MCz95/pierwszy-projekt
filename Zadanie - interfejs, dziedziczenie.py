#!/usr/bin/python

import os.path
from abc import ABC, abstractmethod


class Samochod(ABC):
    def __init__(self, marka, model, kolor):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.czesci = {}

    @abstractmethod
    def dodaj(self, nazwa, cena):
        self.czesci[str(nazwa)] = float(cena)

    @abstractmethod
    def wyswietl(self):
        for el in self.czesci:
            print(f"{el} : {self.czesci[el]}")

    def cena(self, nazwa):
        if nazwa in self.czesci:
            return self.czesci[nazwa]
        else:
            print("Podana czesc nie istnieje.")


class Osobowy(Samochod):
    def __init__(self, marka, model):
        super().__init__(marka, model, "czarny")

    def dodaj(self, nazwa, cena):
        super().dodaj(nazwa, cena)

    def wyswietl(self):
        print(f"Sklep samochod {self.marka} {self.model}")
        if bool(self.czesci):
            super().wyswietl()
        else:
            print("Nie wprowadzono czesci wyposazenia.")


class Autobus(Samochod):
    def __init__(self, marka, model):
        super().__init__(marka, model, "czerwony")

    def dodaj(self, nazwa, cena):
        super().dodaj(nazwa, cena)

    def wyswietl(self):
        print(f"Autobus {self.marka} {self.model}")
        if bool(self.czesci) is True:
            super().wyswietl()
        else:
            print("Brak czesci.")


def main():
    auta = [Osobowy("BMW", "F10"), Osobowy("Audi", "A6"), Osobowy("Chevrolet", "Camaro"), Autobus("Ikarus", "V127.E1"),
            Autobus("Ursus Bus", "Ekovolt"), Autobus("Iveco", "Daily")]

    auta[0].dodaj("tarcze hamulcowe", 399.99)
    auta[0].dodaj("klocki hamulcowe", 149.99)
    auta[1].dodaj("tarcze hamulcowe", 299.99)
    auta[1].dodaj("klocki hamulcowe", 99.99)
    auta[2].dodaj("tarcze hamulcowe", 499.99)
    auta[2].dodaj("klocki hamulcowe", 199.99)
    auta[3].dodaj("tarcze hamulcowe", 359.59)
    auta[3].dodaj("klocki hamulcowe", 119.69)
    auta[4].dodaj("tarcze hamulcowe", 489.99)
    auta[4].dodaj("klocki hamulcowe", 209.29)
    auta[5].dodaj("tarcze hamulcowe", 289.89)
    auta[5].dodaj("klocki hamulcowe", 104.99)

    nr = 1
    for el in auta:
        print(nr, ":")
        el.wyswietl()
        nr += 1
    print(
        f"""\nCena tarcz hamulcowych do samochodu {auta[2].marka} {auta[2].model} wynosi: {auta[2].cena(
            "tarcze hamulcowe")}""")
    print(f"\nCena uszczelki pod glowica do samochodu {auta[2].marka} {auta[2].model} wynosi: ")
    auta[2].cena("uszczelka pod glowica")
    print("")

    print("Dodaj czesc dla wybranego samochodu.")
    nr_auta = int(input("Wybierz samochod z zakresu 1-6: "))
    czesc = input("Podaj nazwe czesci: ")
    cena = input("Podaj cene czesci: ")

    if nr_auta > 0:
        try:
            auta[nr_auta - 1].dodaj(czesc, cena)
            print(f"Dodano czesc {czesc} do auta {auta[nr_auta - 1].marka} {auta[nr_auta - 1].model}")
            if os.path.isfile("c:/sCzesci.txt"):
                with open("c:/sCzesci.txt", 'a') as zawartosc:
                    zawartosc.write(str(f"- {czesc} w cenie {cena} zl do auta {auta[nr_auta - 1].marka} "
                                        f"{auta[nr_auta - 1].model},\n"))
            else:
                print("Plik z danymi sCzesci.txt nie istnieje!")
            if os.path.isfile("c:/sCzesci.txt"):
                print("\nWczesniej dodano nastepujace czesci: ")
                with open("c:/sCzesci.txt", 'r') as zawartosc:
                    print(zawartosc.read().strip())
        except IndexError:
            print("Wprowadzono bledne dane")
    else:
        print("Nie istnieje samochod o numerze 0!")


main()
