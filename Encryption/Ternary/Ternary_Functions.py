
#binary->ternary functions, written in Python for now.
#-----------------------
# Will include ternary not, or, and, xor, and inverse functions
# Will later be expanded to Haskell
#-----------------------
def t_and(t=[]):
	if 0 in t: return 0
	elif 2 in t: return 2
	else: return 1
	
def t_or(t=[]):
	if 1 in t: return 1
	elif 0 in t: return 0
	else: return 2
def t_xor(t=[]):
	if 0 not in t and 2 not in t:
		return 0
	elif 1 in t and 2 in t:
		return 2
	elif 0 in t and 1 in t:
		return 1
	else:
		return 2
	
print t_and([1,2])
