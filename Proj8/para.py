#!/usr/bin/env python3

''' DEKLARACE PROMNĚNÝCH '''
NULA=0
JEDNA=1
DVA=2
''' Konec deklarace '''
''' import knihoven '''
from multiprocessing import Pool
''' konec importu '''

def count(n):
    while n > NULA:
	n -= JENA

pol = Pool(processes=DVA)
pol.map(count, ((10**8), (10**8)))
