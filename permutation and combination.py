from factorial_module import fact
#import factorial from factorial module

n = int(input("Enter n : "))
r = int(input("Enter r : "))

perm = fact(n) / fact(n - r)

comb = fact(n) / (fact(r) * fact(n - r))

print(perm)
print(comb)