import re
def m_eval(num, op, nun):
	if any(char.isdigit() for char in op):
		m_eval(num, "+", int(op))
	elif op=="*": return int(num)*int(nun)
	elif op=="+": return int(num)+int(nun)
	elif op=="/": return int(num)/int(nun)
	elif op=="^": return int(num)**int(nun)
test = "22-3*4/2 + 17"
operators = re.findall("\+|\*|\^|\/|-[0-9]+|[0-9]+", test)
counter=3
if "-" in test:
	for e in range(0, len(operators)):
		if any(char.isdigit() for char in operators[e]) and any(char.isdigit() for char in operators[e+1]):
			operators.insert(e+1, "+")
print operators
a = m_eval(operators[0], operators[1], operators[2])
while counter<len(operators):
	a = m_eval(a, operators[counter], operators[counter+1])
	counter+=2
print a