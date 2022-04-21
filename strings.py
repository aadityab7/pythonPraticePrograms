print("Program Implimenting strings")

user_input = input("Enter a string : ")

print("Type :",type(user_input))

print("printing each indiviual char of string : ")
for i in user_input:
	print(i)

print("\nLength of string :", len(user_input))

print("\nPrinting each char (accessing string using [])")
for i in range(len(user_input)):
	print(user_input[i])

