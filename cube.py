print("Program to calculate the properties of a Cube : ")

from math import sqrt 

class cube :
	def __init__ (Self, a):
		Self.a = a

	def tsa (Self):
		return 6 * Self.a * Self.a

	def lsa (Self):
		return 4 * Self.a * Self.a

	def vol (Self):
		return Self.a * Self.a * Self.a

	def diag (Self):
		return sqrt(3) * Self.a
		
c1 = cube(2)

print("Cube with side :", c1.a, "\nTotal Surface Area :", c1.tsa(), "\nLSA : ", c1.lsa(), "\nVolume : ", c1.vol())
print("Diagonal : ", c1.diag())