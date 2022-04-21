class Calculation:
	def area(self, *args):
		area = "No Arguments Passed"
		if(len(args) == 1):
			area = 3.14 * args[0] * args[0]
		else:
			area = args[0] * args[1]

		return area

item1 = Calculation()
print(item1.area(2.5))
print(item1.area(2,4))