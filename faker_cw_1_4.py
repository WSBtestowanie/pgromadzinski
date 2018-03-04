#!/usr/bin/env python
#-*-coding:utf8-*-

from faker import Faker
fake_pl = Faker('pl_PL')
fake_de = Faker('de_DE')


print "\n  Cwiczenie 1 \n" 

for i in range(10):
	print fake_pl.name()

print "\n  Cwiczenie 2\n"
for i in range(4):
	print fake_pl.address()

print "\n  Cwicznie 3 \n"
for i in range(2):
	print fake_pl.name()
print "\n"
for i in range(2):
	print fake_de.city()
	
print "\n"
for i in range(10):
	print "--" +str(i) +"--"
	print fake_pl.name() +" mieszka na ulicy " +fake_pl.street_name() +" w budynku pod numerem " +fake_pl.building_number() 
 	print " w " +fake_pl.city() +" mieszczacym sie w Polsce" #+fake_pl.country() +"."
	print "Jego kod pocztowy to " +fake_pl.postcode() +"."
	print "Pracuje w firmie " +fake_pl.company() +", do ktorej porusza sie samochodem o rejestracji " +fake_pl.license_plate()+"."
	print "Na codzien kozysta z karty kredytowej o numerze " +fake_pl.credit_card_number(card_type=None) +", waznej do " +fake_pl.credit_card_expire()
	print "Uzywajac kodu CVV: "+fake_pl.credit_card_security_code(card_type=None) +" autoryzuje swoje tranzakcje." 	
	print "\n------------------------------------------------------------------------------------------"
