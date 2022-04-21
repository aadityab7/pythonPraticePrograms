print("Program to calculate factorial using recursion")

def fact(x):
	if(x == 1 or x == 0):
		return 1
	else:
		y = x * fact(x - 1)
		return y

num = int(input("Enter a number to calculate factorial : "))

if(num >= 0):
	fact_val = fact(num)
	print("factorial of", num, "is", fact_val)
else:
	print("Please Enter a positive Integer")