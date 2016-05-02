import re
test = "2-5*2-(-17^3)-3^2"
def m_eval(num, op, nun):
	numer = int(num)
	nuner = int(nun)
	if any(char.isdigit() for char in op):
		m_eval(num, "+", int(op))
	elif op=="*": return numer*nuner
	elif op=="+": return numer+nuner
	elif op=="/": return numer/nuner
	elif op=="^": return numer**nuner
	elif op=="-": return numer - nuner
	else:
		return numer+nuner
def full_eval(test):
	operators = re.findall("\+|\*|\^|\/|-|\(|\)|-[0-9]+|[0-9]+", test)
	counter=3
	if len(operators)>1:
		if "-" in test:
			for e in range(0, len(operators)-2):
				if any(char.isdigit() for char in operators[e]) and any(char.isdigit() for char in operators[e+1]):
					operators.insert(e+1, "+")
				if operators[e]=="-" and operators[e+1]=="-":
					operators[e+2] = "-" + operators[e+2]
					operators.pop(e+1)
		print operators
		b = 0
		if "(" in operators:
			begin = operators.index("(")
			end = operators.index(")")
			stro = operators[begin+1:end]
			p=""
			for e in stro:
				p+=e
			operators = operators[0:begin] + operators[end+1:]
			operators.insert(begin, full_eval(p))
		while True:
			if "^" in operators:
				if int(operators[operators.index("^")+1])%2==0 and "-" in operators[operators.index("^")-1]:
					b = m_eval(operators[operators.index("^")-1], "^", operators[operators.index("^")+1])
					operators.pop(operators.index("^")+1)
					operators.pop(operators.index("^")-1)
					operators.insert(operators.index("^"), "-%s" % (str(b)))
					operators.pop(operators.index("^"))
				else:
					b = m_eval(operators[operators.index("^")-1], "^", operators[operators.index("^")+1])
					operators.pop(operators.index("^")+1)
					operators.pop(operators.index("^")-1)
					operators.insert(operators.index("^"), str(b))
					operators.pop(operators.index("^"))
			else:
				break
		print operators
		if len(operators)>3:
			a = m_eval(operators[0], operators[1], operators[2])
			while counter<len(operators):
				a = m_eval(a, operators[counter], operators[counter+1])
				counter+=2
			return a
		elif len(operators)==2 and operators[0]=="-":
			a = -1 * int(operators[1])
			return str(a)
	else:
		print operators[0]


a = full_eval(test)
print "---------------"
print a
