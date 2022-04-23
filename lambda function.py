#Using Lambda Function : 
z = lambda x,y : x + y
print(z(2,3))


#Filter Method: 

def even(n):
	return n % 2 == 0

list1 = [2,13,42,4,524,331,452,321,22]


list_even = []

print(list1)
print(list_even)


for i in list1:
	if i % 2 == 0: 
		list_even.append(i)


for i in list1:
	y = even(i)
	if y == True:
		list_even.append(i)

print(list_even)


list_even = list(filter(even, list1))

#usually used with big data :
#using Inline Lambda function instead of normal function: 

list_even2 = list(filter(lambda x : x % 2 == 0, list1))
list_odd = list(filter(lambda x : x % 2 != 0, list1))

print(list1)
print(list_even)
print(list_even2)
print(list_odd)


#Map Function : 

list_even_mapped = list(map(lambda x : x * 2, list_even))
print(list_even_mapped)