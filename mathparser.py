import re
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
test = "2-5*2--17^3-3^2"
operators = re.findall("\+|\*|\^|\/|-|-[0-9]+|[0-9]+", test)
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
	
	a = m_eval(operators[0], operators[1], operators[2])
	while counter<len(operators):
		a = m_eval(a, operators[counter], operators[counter+1])
		counter+=2
	print a
	#fix subtraction in exponents
	#add parentheses
else:
	print operators[0]
