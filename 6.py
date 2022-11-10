## Dictionary
from pprint import pprint

employee = {
    'name' : 'Aman',
    'emp_id' : 123432,
    'exp' : '3.5 yr',
    'name': 'abc' 
}

pprint(employee)


print(employee['name'])

print(employee.keys())

employee['name'] = 'Aman'

pprint(employee)

employee['location'] = 'India'

pprint(employee)

employee.pop('exp')

pprint(employee)

employee.popitem()

pprint(employee)

### copy dict

employee_bkp = employee

print(employee_bkp)

employee['exp'] = '3.5 yr'

print(employee_bkp)

employee_bkp = employee.copy()

print(employee_bkp)

employee.pop('exp')

print(employee_bkp)

print(employee)




