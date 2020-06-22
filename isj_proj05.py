#!/usr/bin/env python3

# DEKLARACE ZÁSTUPNÝCH PROMNĚNÝCH 
NULA=0
JEDNA=1
DVA=2
# Konec deklarace
'''		Třída Polynomial pro zpracování ruzných polynomů, dle zadání 	''' 
class Polynomial:
	'''		Definife funkce __INIT__, uprava dat pro další operace/funkce	'''
	def __init__(self, *args, **arg):							# Definitce funkce __INIT__
		self.polynom = []										# Deklarace 
		if args:											 	# podmínka na zjistění jestli byl vložen list
			if len(args) != NULA and type(args[NULA]) == list: self.polynom = args[NULA].copy()	# pokud to je list a není nulový  Tak se skopíruje hlubokou kopii
			else: [self.polynom.append(i) for i in args]			# projetí všech hodnot a přidání hodnoty self.polynom
		if arg:													# jestli že to není list
			for i in list(arg):									# projetí  všech klíču
				if arg[i] != NULA:								# když se nerovná nule 
					while len(self.polynom) <= (int(i[JEDNA:])): self.polynom.append(NULA)  # projetí všech položek přidání hodnot
					self.polynom[int(i[JEDNA:])] = arg[i]		# přidání zbytku a kontrola
					
	def __str__(self):
		'''	 Funkce pro tisk která upravu výstupní data	 '''
		vysledek = ""											# deklarace 					
		if not len(self.polynom): return "0" 					# jestliže je pole nulové vrátí nulu																			
		for i, koefi in enumerate(reversed(self.polynom)):		# projetí všech hodnot
			if koefi: 											# koeficiont
				if koefi < NULA: znam, koefi = (' - ' if vysledek else '- '), -koefi # jestli že je konficient záporný 
				elif koefi > NULA: znam = (' + ' if vysledek else '') #jestli že je kladný
				str_koefi = '' if koefi == JEDNA and (len(self.polynom) - (i + JEDNA)) != NULA else str(koefi)              
				if (len(self.polynom) - (i + JEDNA)) == NULA: str_mocnina = ''	# jestliže je mocnina rovná nule					
				elif (len(self.polynom) - (i + JEDNA)) == JEDNA: str_mocnina = 'x' # jestliže je mocnina rovná 1
				else: str_mocnina = ('x' + '^' + str((len(self.polynom) - (i + JEDNA)))) # výpočet											 
				vysledek += (znam + str_koefi + str_mocnina) 	# výpočet
		return vysledek        
		
	def __eq__(self, dalsi):
		'''		porovnání na zjištění velkosti	 '''
		if type(dalsi) == Polynomial and  self.polynom == dalsi.polynom: return True		# podmínka jestli je to Polynomial a zd podmínka zda-li se rovnají
		return False		

	def __add__(self, dalsi):
		'''		Přídání jednoho polinomu do ruhého nebo opačně dle délky	'''
		list = [] 												# deklarace listu
		if len(self.polynom) > len(dalsi.polynom): [dalsi.polynom.append(NULA) for i in range((len(self.polynom) - len(dalsi.polynom)))] # podmínka na zjistění velikosti, přidání hodnot do
		else: [self.polynom.append(NULA) for i in range((len(dalsi.polynom) - len(self.polynom)))]		# přidání hodnot do 
		[list.append(self.polynom[i] + dalsi.polynom[i]) for i in range(len(self.polynom))]	# projetí a  sloužení do jedného        
		return Polynomial(list)									# návrat list

	def __mul__(self, dalsi):
		'''  	násobení polynomu a návrat jeho nové hodnoty	'''
		list = ([NULA] * ((len(self.polynom) + len(dalsi.polynom)) - JEDNA))						# vyvtoření pole
		for i in range(len(self.polynom)):															# projetí 2x cyklu
			for j in range(len(dalsi.polynom)):	list[i + j] += (self.polynom[i] * dalsi.polynom[j]) # naplnění pole vypočtem
		return Polynomial(list)																		# návrat listu 

	def __pow__(self, mocnina):
		'''	 projíždí je je mocnina a podle toho vykoná operaci nad daty v polinomu '''
		if mocnina == NULA:	 return Polynomial(JEDNA)				# jestli je mocnina =0, return 1
		elif mocnina >= JEDNA:										# porovnání jestli je mocnina větší než 0		       
			if mocnina == JEDNA: return self						# jestli je mocnina = 1, return to co přišlo do funkce
			else:
				vysledek = self										# první číslo
				mocnina += JEDNA									# upravení mocniy
				for i in range(DVA, mocnina): vysledek = (vysledek * self) # naplnění zbytkem čísel
				return vysledek										# návrat hodnoty
		return NULA

	def derivative(self):
		'''		Funcke pro derivaci polynomu 	'''
		derivace = []											# Deklarace listu pro výsldek
		[derivace.append((self.polynom[i] * i)) for i in range(JEDNA, len(self.polynom))] # Projetí pole od druhého indexu  a zdeerivace u všech položek a návrat do listu
		return Polynomial(derivace)								# Návrat po derivaci

	def at_value(self, *arg):
		''' Funkce pro přidání hodnoty '''
		hodnota =NULA											# deklarace
		hodnota1=NULA											# deklarace 
		if len(arg) == JEDNA:									# velikost argumentu  == 1
			for i in range(len(self.polynom)): hodnota += (self.polynom[i] * (arg[NULA] ** i))	# přiřazení všechn hodnot do listu				 
			return hodnota										# návrat honoty
		elif len(arg) == DVA:									# velikost argumentu  == 2
			for i in range(len(self.polynom)):					# projetí pole
				hodnota += (self.polynom[i] * (arg[NULA] ** i))	 # přiřazení do první
				hodnota1 += (self.polynom[i] * (arg[(NULA+JEDNA)] ** i)) # přiřazení do druhé         
			return (hodnota1 - hodnota) 						# návrat rodílu
		else: return NULA										# nevyhovující stav
		
def test():
	''' Funkce pro otestování všech funkcí ve tříde Polynomial '''
	assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"  
	assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
	assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
	assert str(Polynomial(x2=0)) == "0"
	assert str(Polynomial(x0=0)) == "0"
	assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
	assert Polynomial(x2=0) == Polynomial(x0=0)
	assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
	assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
	pol1 = Polynomial(x2=3, x0=1)
	pol2 = Polynomial(x1=1, x3=0)
	assert str(pol1+pol2) == "3x^2 + x + 1"
	assert str(pol1+pol2) == "3x^2 + x + 1"
	assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
	assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
	pol3 = Polynomial(x0=-1,x1=1)
	assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
	assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
	assert str(Polynomial(x0=2).derivative()) == "0"
	assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
	assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
	pol4 = Polynomial(x3=2,x1=3,x0=2)
	assert str(pol4.derivative()) == "6x^2 + 3"
	assert str(pol4.derivative()) == "6x^2 + 3"
	assert Polynomial(-2,3,4,-5).at_value(0) == -2
	assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
	assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
	pol5 = Polynomial([1,0,-2])
	assert pol5.at_value(-2.4) == -10.52
	assert pol5.at_value(-2.4) == -10.52
	assert pol5.at_value(-1,3.6) == -23.92
	assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
	test()
