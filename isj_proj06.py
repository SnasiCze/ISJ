#!/usr/bin/env python3

# DEKLARACE ZÁSTUPNÝCH PROMNĚNÝCH 
NULA=0
JEDNA=1
DVA=2
TRI=3
CTYRI=4
# Konec deklarace
# import knihoven
import copy
import itertools
# konec importu

def first_nonrepeating(text):
	''' Funkce vrací první písmeno které se v řetězci neopakuje '''
	tmp = {}				#Deklarace dict
	if type(text) == str:	#Zistění jestli se jedná o řetězec 
		if len(text) == JEDNA:	#Pokud je delka řeezce 1
			if text.isalpha() or text.isdigit(): return text
			else: return None # pokud to není p1ísmeno
		for pismeno in text:	# projetí celého řetězce
			if pismeno in dict.keys(tmp): tmp[pismeno] += JEDNA # jestli už bylo to písmeno v poli tak k němu přičti 1
			else: tmp[pismeno] = JEDNA #když tan to písmeo ještě nebylo
		for klic, hodnota in zip(dict.keys(tmp), dict.values(tmp)): #projetí dict(key,value)
			if hodnota == JEDNA:	# to písmeno co je tam je jedno tak vrať 
				return klic		# navrátí písmeno
	return None #nebyl to řetězec
def combine4(listcisel, vysledek):
	''' Funkce vrací všechny možné způsoby vypočtení daného číla z daných čísel '''	
	operant = ["+", "-", "*", "/"] 			# operandy povoleny ze zadání
	kombinace = []							# list všech možných kombinací ! Ne však správných
	duplikant = []							# list na odstranění duplikací z kombinaci
	reseni = []								# vysledný list
	if type(listcisel) != list or len(listcisel) != CTYRI or type(vysledek) != int:  return reseni 	# korekce vstupu
	for polozka in listcisel:																   		# Projetí cyklu
		if type(polozka) != int: return reseni												   		# jestliže alespoň jeden prvek není int, řešení neexistuje
	for perm in itertools.permutations(listcisel, CTYRI):									   		# Permutace všech vstupních hodnot z listu 
		#for i,j,k in zip(range(len(listcisel)), range(len(listcisel)), range(len(listcisel))):		# Projetí listu pro i, j , k	
		for i in range(len(listcisel)):
			for j in range(len(listcisel)):
				for k in range(len(listcisel)):
					# xoxoxox - x reprezentuje číslo, o reprezentuje operator
					kombinace.append(str(perm[NULA]) + operant[i] + str(perm[JEDNA]) + operant[j] + str(perm[DVA]) + operant[k] + str(perm[TRI]))
					# (xox)oxox - zavorka na zacatku
					kombinace.append("(" + str(perm[NULA]) + operant[i] + str(perm[JEDNA]) + ")" + operant[j] + str(perm[DVA]) + operant[k] + str(perm[TRI]))
					# xoxo(xox) - zavorka na konce
					kombinace.append(str(perm[NULA]) + operant[i] + str(perm[JEDNA]) + operant[j] + "(" + str(perm[DVA]) + operant[k] + str(perm[TRI]) + ")")
					# xo(xox)ox - zavorka uprostred
					kombinace.append(str(perm[NULA]) + operant[i] + "(" + str(perm[JEDNA]) + operant[j] + str(perm[DVA]) + ")" + operant[k] + str(perm[TRI]))
					# (xox)o(xox) - zavorky na začátku a konci
					kombinace.append("(" + str(perm[NULA]) + operant[i] + str(perm[JEDNA]) + ")" + operant[j] + "(" + str(perm[DVA]) + operant[k] + str(perm[TRI]) + ")")
					# (xoxox)ox - trojitá závorka na začátku
					kombinace.append("(" + str(perm[NULA]) + operant[i] + str(perm[JEDNA]) + operant[j] + str(perm[DVA]) + ")" + operant[k] + str(perm[TRI]))
					# xo(xoxox) - trojitá závorka na konci
					kombinace.append(str(perm[NULA]) + operant[i] + "(" + str(perm[JEDNA]) + operant[j] + str(perm[DVA]) + operant[k] + str(perm[TRI]) + ")")
					# ((xox)ox)ox - vnoření na začatku závorek
					kombinace.append("((" + str(perm[NULA]) + operant[i] + str(perm[JEDNA]) + ")" + operant[j] + str(perm[DVA]) + ")" + operant[k] + str(perm[TRI]))
					# xo(xo(xox)) - vnoření na konci závorek
					kombinace.append(str(perm[NULA]) + operant[i] + "(" + str(perm[JEDNA]) + operant[j] + "(" + str(perm[DVA]) + operant[k] + str(perm[TRI]) + "))")
					# (xo(xox))ox - vnoření středu do začátku
					kombinace.append("(" + str(perm[NULA]) + operant[i] + "(" + str(perm[JEDNA]) + operant[j] + str(perm[DVA]) + "))" + operant[k] + str(perm[TRI]))
					# xo((xox)ox) - vnoření středu do konce
					kombinace.append(str(perm[NULA]) + operant[i]+ "((" + str(perm[JEDNA]) + operant[j] + str(perm[DVA]) + ")" + operant[k] + str(perm[TRI]) + ")")
	# odstranení duplikantů
	for i in kombinace:								# projetí listu kombnací
		if i not in duplikant: duplikant.append(i) 	# jestli se nenachází v listu duplikant, tak ho tam přidá							 
	# porovnání hodnot s vysledek a přidání do pole
	#print(duplikant)
	#print(len(duplikant))
	try:																	# konstrukce try-except, kvůli dělení nulou
		for i in range(len(duplikant)):										# projetí všech neduplikovaných hodnot
			if eval(duplikant[i]) == vysledek: reseni.append(duplikant[i])	# porovnání příkladu a vysledku, pokud se rovnají je to jeden z výsledku	
	#		print(eval(duplikant[i]))
	except:	pass	# except -> když try někde spadl, pass -> nedělej nic
	if len(reseni) >= JEDNA: return reseni		# když řešení je větší rovno 1, vrať řešení s výsledkem
	return reseni								# Návrat prázdné hodnoty

			
def test():
	''' Funkce na otestování některých z možných vstupů '''
	assert first_nonrepeating("tooth") == 'h'
	assert first_nonrepeating("lool") == None
	assert first_nonrepeating('h') == 'h'
	assert first_nonrepeating(123) == None
	assert first_nonrepeating('\t') == None
	assert first_nonrepeating(' ') == None
	assert combine4([6,6,5,2],25) == []
	#print(combine4([6,6,5,2],36))
	#assert combine4([6,6,5,2],36) == ['(2+5)*6-6', '(5+2)*6-6', '6*(2+5)-6', '6*(5+2)-6']

if __name__ == '__main__':
	test()
