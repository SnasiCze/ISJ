#!/usr/bin/env python3

# Vrátí vstupní položku item, pokud tato může být prvkem množiny v Pythonu, v opačném případě frozenset(item)
#"""  Pomocí kontroly datových typů se program větví na 2 části return item a retun frozenset(item) """
def can_be_a_set_member_or_frozenset(item):
	"""  Pomocí kontroly datových typů se program větví na 2 části return item a retun frozenset(item) """
	if type(item) == list:
		return frozenset(item)
	elif type(item) == dict:
		return frozenset(item)	
	else:
		return item

		
# Na vstupu dostane seznam a pouze s použitím vestavěných funkcí (tedy bez použití "import") z něj vytvoří seznam, odpovídající množině všech podmnožin, tedy např.	
def all_subsets(lst): 		
	'''  Pomocí bitových posunů si pohlídám zprávné zapsání a pak už jen přidávám do listu '''
	list = []
	for i in range(1 << len(lst)):
		subset = [lst[bit] for bit in range(len(lst)) if i & (1 << bit) > 0]
		list.append(subset)		
	return list


#obdoba předchozího, ale při volání dostane prvky seznamu přímo jako argumenty a navíc má volitelný parametr exclude_empty, který, když není ve volání uveden, nebo je jeho hodnota True, vrátí výsledek bez prázdného seznamu. Pokud je hodnota tohoto argumentu False, je výsledek stejný jako u předchozí funkce.

def all_subsets_excl_empty(*args, **arg):
	''' Z argumetu funkce si přečtu nejprve všechny argumenty a pak se rozhoduji. nejprve provedu funkci "all_subsets" a pak dle exclude_empty rozhoduji co vrátím '''
	listtmp = all_subsets(list(args))
	if not arg:	
		del listtmp[0]
		return listtmp
	elif arg['exclude_empty'] == False:
		return listtmp
	elif arg['exclude_empty']:
		del listtmp[0]
		return listtmp
def test():
	''' test funkce "can_be_a_set_member_or_frozenset" '''
	assert can_be_a_set_member_or_frozenset(1) == 1
	assert can_be_a_set_member_or_frozenset((1,2)) == (1,2)
	assert can_be_a_set_member_or_frozenset([1,2]) == frozenset([1,2])
	
	''' test funkce "all_subsets" '''
	assert all_subsets(['a', 'b', 'c']) == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]

	''' test funkce "all_subsets_excl_empty" '''
	assert all_subsets_excl_empty('a', 'b', 'c') == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
    #assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty = True) == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
	assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty = False) == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
	
if __name__ == '__main__':
    test()