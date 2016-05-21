
#binary->ternary functions, written in Python for now.
#-----------------------
# Will include ternary not, or, and, xor, and inverse functions
# Will later be expanded to Haskell
#-----------------------
def to_int(st=""):
	num = 0
	p = 0
	for tit in st[::-1]:
		num += int(tit)*3**p
		p += 1
	return num
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
def t_not(t=2):
	if t==0: return 1
	elif t==2: return 2
	else: return 0

print to_int("201") #should be 19 and is