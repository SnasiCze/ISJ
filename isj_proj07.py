#!/usr/bin/env python3
'''
# Autor: Daniel Snášel
# Datum: 21.04.2018
# Soubor: isj_proj07_xsnase06.py
'''
''' DEKLARACE ZÁSTUPNÝCH PROMNĚNÝCH '''
NULA=0
JEDNA=1
DVA=2
TRI=3
CTYRI=4
''' Konec deklarace '''
''' import knihoven '''
import math
''' konec importu '''


class TooManyCallsError(Exception):
	''' Třída TooManyCallsError pro generování chybové zpávy '''
	def __init__(self, zprava):
		''' Konstruktor chybové zprávy '''
		self.zprava = zprava;

def limit_calls(max_calls=DVA, error_message_tail='called too often'):
	''' Dekodér limit_calls, max_calls je maximalní pocer volání funkce, error_message_tail vypis teto zpávy při větším počtu volání než je max_calls '''
	def _limit_calls(parametr):
		''' funkce pro návrat funkce cteni + nulování poctu cteni'''
		def cteni(a, b):
			''' funkce pro zjištěni počtu čtení a vyhodnocení nového čtení '''
			if cteni.calls < max_calls:
				cteni.calls += JEDNA
				return parametr(a, b)
			else: raise TooManyCallsError('function "'+parametr.__name__+'" - '+str(error_message_tail))
		cteni.calls = 0
		return cteni
	return _limit_calls
	
@limit_calls(1, 'that is too much')
def pyth(a,b):
	''' funkce na výpočet pythagorovi věty dle zadání '''
	return math.sqrt(a**DVA + b**DVA)
	
def ordered_merge(*args, selector=None):
	''' funkce postupně generuje prvky, args -> zvolení generování, selector -> poradi generovani ze vstupu, return -> navrat prvu v danem pořadí '''
	tmp = []
	if selector is not None:
		if selector.__len__() is not NULA:
			def iterate(prvek):
				''' iteruje/generuje prvky na základě vstupních dat '''
				for i in prvek:
					try: yield i
					except: raise StopIteration
			[tmp.append(iterate(prvek)) for prvek in args]
			for j in range(selector.__len__()): yield next(tmp[selector[j]])
	return []
		
class Log():
	''' trida log, zapisuje do soubor vybrané data '''
	def __init__(self, soubor):
		''' soubor, značí jaký soubor má být otevřen '''
		self.f = open(soubor, 'w')
		#with open(soubor, 'w') as outfile, open(outfile, 'r', encoding='utf-8') as infile:
		#	outfile.write()
	def __enter__(self):
		''' zápis do souboru '''
		self.f.write('Begin\n')
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		''' ukoncenu zápisu do souboru a přidání konce '''
		self.f.write('End\n')
		self.f.close()

	def logging(self, parametry):
		''' zápise do souboru to co je v poarametru funkce '''
		self.f.write(parametry + "\n")
