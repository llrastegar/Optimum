
#binary->ternary functions, written in Python for now.
#-----------------------
# Will include ternary not, or, and, xor, and inverse functions
# Will later be expanded to Haskell
#-----------------------
def t_and(t=[]):
	print t
	if 0 in t: return 0
	elif 1 in t: return 1
	else: return 2
	
def t_or(t=[]):
	print t
	if 1 in t: return 1
	elif 0 in t: return 0
	else: return 2
	
print t_and([1,2,2])
