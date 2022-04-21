print("\nProgram to Impliment Function OverRiding using classes and methods : \n")

class A:
	def random(self):
		print("In class A")

class B(A):
	def random(self):
		print("In class B")

obj1 = A
obj2 = B

obj1.random()
obj2.random()