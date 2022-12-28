############ functions

### creation of functin 
def example_header(eg_number):
    # eg_number is having value 4 
    print("#####################", end="\n\n")

    print(f"Example-{eg_number}")


### calling of function

example_header(1)


### compulsory mutliple arguments 

example_header(2)

def add_employee(name,emp_id,designation):
    print(f'Name : {name}')
    print(f'Employee : {emp_id}')
    print(f'Designation : {designation}',end='\n\n')


add_employee('Aman',1111,'DevOps')

add_employee(emp_id=2222,name='Karthik',designation='DevOps')

## add_employee(emp_id=2222)

# above statement will give below error
# Traceback (most recent call last):
#   File "10.py", line 30, in <module>
#     add_employee(emp_id=2222)
# TypeError: add_employee() missing 2 required positional arguments: 'name' and 'designation'

### optional mutliple arguments 

example_header(3)

def add_employee(name='None',emp_id='None',designation='None'):
    print(f'Name : {name}')
    print(f'Employee : {emp_id}')
    print(f'Designation : {designation}',end='\n\n')


add_employee()

add_employee('Aman')

add_employee('Aman',1111)


### Dynamic Argument 

example_header(4)


def add_employee(*emp_details):
    for i in emp_details:
        print(i)
    print(f'Name : {emp_details[0]}')
    print(f'Employee : {emp_details[1]}')
    print(f'Designation : {emp_details[2]}',end='\n\n')


add_employee('Aman',1111,'DevOps','Delhi','ABC Corp')


### dynamic  arguments with key values



example_header(5)


def add_employee(**emp_details):
    # print(emp_details)
    for key, value in emp_details.items():
        print(f"{key} : {value}")

add_employee(age=25,name='Aman',designation='DevOps',city='Delhi',org='ABC Corp')



## Return in function

example_header(6)

def add(*input):
    print(input)
    c=0
    for i in input:
        c = c + i
    return c

output = add(2,3,4,5,12,13)

print(output)

def div(*input):
    print(input)
    c=0
    count = 0
    for i in input:
        if count == 0:            
            c=i
        else:
            c = c / i
        count+=1
    return c

output = div(2,3)


