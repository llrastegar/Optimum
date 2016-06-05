
import re
test = "2-(5*2)+3-(17^(3+2))+(6*(7*5*(3+3)))+5+7*(1*2)"

def m_eval(l, op, q):
	n = int(l)
	j = int(q)
	if op=="*": return n*j
	elif op=="/": return n/j
	elif op=="^": return n**j
	elif op=="+": return n+j
	elif op=="-": return n-j
	elif op=="%": return n%j
	else: return n*j

def t_s(t=[]):
	l=""
	for e in t:
		l+=str(e)
	return l
def full_eval(test):
	operators = re.findall("\+|\*|\^|\/|-|\(|\)|-[0-9]+|[0-9]+", test)
	out=0
	if "(" in operators:
		while "(" and ")" in operators:
			a = operators.index("(")
			b = operators.index(")")
			if "(" not in operators[a+1:b]:
				insert = full_eval(t_s(operators[a+1:b]))
				operators = operators[:a] + operators[b+1:]
				operators.insert(a, insert)
				if "(" not in operators:
					out = full_eval(t_s(operators))
			else:# this function only looks for one pair of parentheses within another
				smallop = operators[a+1:b] # it should look for more
				z=0
				for e in smallop:
					if e=="(":
						w = z
					z+=1
				insert = full_eval(t_s(smallop[w+1:b]))
				operators = operators[:w+a+1] + operators[b+1:]
				operators.insert(a+w+1, insert)
	else:
		out = m_eval(operators[0], operators[1], operators[2])
		if len(operators)>3:
			e=2
			while e<(len(operators)-1):
				if e<5:
					out = m_eval(out, operators[e+1], operators[e+2])
					#print operators
					e+=3
					#print out
				else:
					out = m_eval(out, operators[e], operators[e+1])
					e+=2
			return str(out)
		else:
			return str(out)
	return out


print full_eval(test)
