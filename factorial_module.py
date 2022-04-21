#Factorial Module : 

def fact(x):
	if(x == 1 or x == 0):
		return 1
	else:
		y = x * fact(x - 1)
		return y