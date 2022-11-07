# str
# int, float
# list, tuple , dict, set , bool

from re import T
from sre_constants import SUCCESS


a=22.5
product = ['erp','cms','hr'] #it's a list

print(type(a))
print(type(product))

#####
## arthmetic operator
## ** -> exponential
## % -> modulus

p=10
q=3
c=p**q
print(c)

#####

p=10
q=3

p = p + q
print(p)
p += q
print(p)

p -= 3 # -> p = p - 3
print(p)



#### Comparision Operators

a = 2
if a >= 3:
    print("Success")


#### Logical Operators

# AND 

# T & T = T
# F & T = F
# T & F = F
# F & F = F

a = 2 
b = 4

print(a == 2 and b == 3)

if a == 2 and b == 3:
    print("success")
else:
    print("failure")


###########
a = 2 
b = 4
c = 5
d = 6

print((a >= 2 and b <= 3) or (c >= 5 and d <= 6))

if (a >= 2 and b <= 3) or (c >= 5 and d <= 6):
    print("success")

# (a >= 2 and b <= 3) or (c >= 5 and d <= 6)

# ( T and F ) or (T and  T )

# F or T

# T

print("======== Identity Operator ===========",end="\n\n")
## when both the variable have same object 

x = 2
y = 3
z = x

print(x is not y)

print(z is x)

print(z)
print(x)
if x is y:
    print("success")

#####
## membership operator 

print("======== membership operator ===========",end="\n\n")


product = ['erp','cms','hr']

if "hr" in product:
    print("Success")

if "finance" not in product:
    print("Success")

## to check subset of a particular string

output = "this test is a Success"

if "success" in output.lower():
    print("yes I do have success keyword in output string")


##### type casting 

x = 1

y=str(x)

print(x)
print(type(x))
print(y)
print(type(y))

x = "1"
y = int(x)

a = 2.34
b = int(a)

p = "1.5"
q = float(p)