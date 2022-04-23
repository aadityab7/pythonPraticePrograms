#three types of methods:
#1. Instance Method
#2. Static Method
#3. Class Method

class Student(object):
	"""Student Class"""
	institution = "IIPS"

	def __init__(self, a, b):
		self.a = a
		self.b = b

	#Instance Method: 
	def show(self):
		print("-------------------------------")
		print("Marks in Python = ", self.a)
		print("Marks in Python Lab = ", self.b)
		print("-------------------------------")

	#Class Method: for accesing the class asssociated variables
	@classmethod
	def info(self):
		print("Class belongs to", self.institution)

	#Static Method 
	@staticmethod
	def about():
		print("This class holds the data of marks obtained by students in python and it's lab in IIPS")

s1 = Student(12, 10)
s2 = Student(13, 11)
s3 = Student(14, 19)
s1.show()
s2.show()
s3.show()
Student.info()
Student.about()
print(Student.institution)
		