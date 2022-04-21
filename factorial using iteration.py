print("Program for calculating Factorial using iteration :")

def fact(x):
	fac = 1
	if(x == 1 or x == 0):
		return fac
	for i in range(1, x + 1, 1):
		fac = i * fac
	return fac

user_input_number = int(input("Enter a integer : "))

print("Factorial of", user_input_number, "is", fact(user_input_number))

