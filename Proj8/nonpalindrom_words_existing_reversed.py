#!/usr/bin/env python3

''' import knihoven '''
import fileinput
''' konec importu '''
''' DEKLARACE ZÁSTUPNÝCH PROMNĚNÝCH '''
MJEDNA=-1
''' Konec deklarace '''
''' DEKLARACE PROMNĚNÝCH '''
words = palin = set()
''' Konec deklarace '''
for line in fileinput.FileInput():
	tmp = line.rstrip()
	words.add(tmp)
	if tmp == tmp[::MJEDNA]: palin.add(tmp)

vysledny = [w for w in words if w not in palin and w[::MJEDNA] in words]
print(sorted(vysledny))
