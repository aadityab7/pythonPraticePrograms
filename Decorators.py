from Decorators_support import *

print("Program to Impliment the Decorator Functions : \n")

#decorators are functions through which we can modify the functioning of another function
#when we don't have the control to change the function defination  
#Decorator : -----------------------------------------------------------------------------
def smart_div(funct):
	#the number of params of inner fun and funct must be same : 
	#inner_fun stores the modified function: 
	
	def inner_fun(m, n):
		if(m < n):
			m, n = n, m
		return funct(m, n)

	return inner_fun

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

c = div(a,b)

d = smart_div(div)
result = d(a,b)

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", result)