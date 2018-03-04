#!/usr/bin/env python
#-*- coding: utf-8 -*-
from faker import Faker
fake = Faker()

print "Program generuje dane których liczba i rodzaj jest zdefiniowana przez urzytkowniaka. Dane zapisywane są w pliku tekstowym o nazwie zdefiniowanej przez urzytkownika."
print "Kolumny są oddzielone kropkami, informacje o kolejnych osobach zapisywane w nowych wierszach, jena osoba jeden wiersz."



j = raw_input("jakie dane chcesz wygenerować? \n \n Wpisz pokolei bez spacji litery które będą odpowiadać: \n \n i -imie, n - nazwisko, u - ulica, d -nr domu, m - miasto, t - nr telefonu: \n ")
tablica_j = []
#dlugosc = len(j)
#print dlugosc

for index in range(len(j)):
	tablica_j.append(j[index])
print tablica_j
	

i = input("Podaj jaką liczbę wierszy danych do wygenerowania ktore mam wygenerowac: ")

n_plik = raw_input("Proszę podaj nazwę pliku razem z rozszeżeniem w kórym chcesz zapisać dane: ")


def faker_create(data, fake):
	out_data="przykaladowy tekst"
	if data == "i":
		out_data = fake.first_name()
	if data == "n":
		out_data = fake.last_name()
	if data == "u":
		out_data = fake.street_name()
	if data == "d":
		out_data = fake.building_number()
	if data == "m":
		out_data = fake.city()
	if data == "t":
		out_data = fake.phone_number()
	return out_data

tablica_wynikowa = []

def wiersz_tablicy (tablica_j, fake):
	tablica_wynikowa = []
	for pozycja in tablica_j:
		dodaj_pozycje = faker_create(pozycja, fake)
		tablica_wynikowa.append(dodaj_pozycje)
		print tablica_wynikowa
	return tablica_wynikowa
tablica_w =[]

for d in range(i):
	tablica_w.append(wiersz_tablicy(tablica_j, fake))


plik = open(n_plik, 'w')
plik.write(str(tablica_w)) 
#tab_dane = [imie, nazwisko, nr_domu, miasto, nr_telefonu]	
#print tab_dane	
