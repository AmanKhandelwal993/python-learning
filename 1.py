name='karthik'

print(f"Hi It is {name}.")
print("Hi It is "+name+".")

# ways to assign values in variable 

role,experience,dob = "DevOps" ,"3yrs" , "03-04-99"
emp_id = a = b = "23451"
product = ['erp','cms','hr'] #it's a list
x,y,z = product

print(emp_id)
print(product)
print(x,y,z)
print(x+y+z)

###############
## Global Variable
###############


p = 22 #global variable

def add():
    p = 10 #local variable
    print(p)

add()
print(p)