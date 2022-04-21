print("\nProgram to Impliment Function Overloading using methods of a class : \n")

class student:

	#The following is a function that can barely achive function overloading
	def average(self, a = None, b = None, c = None):
		average = 0
		if(a != None and b != None and c != None):
			average = (a + b + c) / 3
		elif(a != None and b != None and c == None):
			average = (a + b) / 2
		elif(a != None and b == None and c == None):
			average = a
		else:
			average = "No Values Provided"

		return average

	#-------------
	#The following is the function that Efficiently Achives the Function Overloading:
	#-------------
	def avg(self, *x):
		average = 0
		sum = 0
		if (len(x) == 0):
			average = "No Values Provided"
		else:
			for i in x:
				sum += i
			average = sum / len(x)

		return average

item1 = student()
print(item1.average(12, 13, 14))
print(item1.average(1,2))
print(item1.average())
print(item1.avg(1, 2, 3, 4, 5))
print(item1.avg())