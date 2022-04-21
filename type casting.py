print("\nProgram for type casting\n")

user_input = input("Enter a integer : ")
user_input2 = input("Enter a float number : ")

print("Type of Inputs :", type(user_input), "and", type(user_input2))

print("All user inputs are stored as string")
print("We need to change thier type to numbers to perform arithemetic operations on them")

num = int(user_input)
num2 = float(user_input2)

print("After Type casting :", type(num), "and", type(num2))

print(user_input, "+", user_input2, "=", num + num2)

print("We can also type cast numbers into strings")

result = num + num2
print("Before type casting :", result, "is of type :", type(result))

result = str(result)
print("After type casting :", result, "is of type :", type(result))

print("All data types are implicitly type casted to string for output")