print("\nProgram to impliment classes and object functionality in python\n")
class circle:
	def __init__(Self, r):
		Self.r = r

	def area(Self):
		return 3.14 * Self.r * Self.r

	def circumference(Self):
		return 2 * 3.14 * Self.r

c1 = circle(3)
c2 = circle(2.5)

print("circle with radius :", c1.r,":",c1.area(), c1.circumference())
print("circle with radius :", c2.r,":",c2.area(), c2.circumference())