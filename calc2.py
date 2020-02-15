import re

class Calculator(object):
	
	def multiply_divide(self, slicey):
		problem = slicey.split()
		while len(problem)>1:
			if problem[1]=='/':
				prod = float(problem[0]) / float(problem[2])
			elif problem[1]=='*':
				prod = float(problem[0]) * float(problem[2])
			problem[0] =  prod
			del problem[1:3]
			continue	
		
		return str(problem[0])


	def evaluate(self, string):
		problem = re.split('\- |\+ ', string.strip())
		solution = ''
		for part in problem:
			solution += self.multiply_divide(part.strip())
			if string.index(part)+len(part) < len(string):
				solution+=string[string.index(part)+len(part)]
		sliced_again = re.split('\-|\+', solution)
		result = float(sliced_again[0])
		actions = ''
		for ch in solution:
			if ch in '+-':
				actions+=ch

		for number in sliced_again[1:]:
			if actions[sliced_again.index(number)-1] == '-':
				result-= float(number)
			else:
				result+=float(number)

		return result







C = Calculator()
print(C.evaluate('12 / 2 * 3 + 34 * 4 - 6'))