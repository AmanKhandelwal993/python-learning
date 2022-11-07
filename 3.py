# list 
# tuple
# set
# dictionary
# strings



# list -> ordered, changable, and value can be duplicated 


from pprint import pprint


products = ['smartphone', 'printer', 'mouse', 'smartphone']

print(products)

## blank list/ empty list

products = []

print(products)

products = ['smartphone', 'printer', 'mouse', 'monitor', 'computer', 'pendrive']

## the first item has index 0 

print("first item of the list at 0 index")
print(products[0])

print(products[2])

## to print the range of index a to b, [a:b+1] 

### products[1:4] in this range the 4 index position value will be ignored

print(products[1:4])

### for first n values 

print(products[:3])

### print from  last values 

print(products[3:])

#### -1 represent the last element of the list 
print(products)

print(products[-1])

## 

print(products[-3:-1])

### for last n values 

print(products[-3:])


### 

products = ['smartphone', 'printer', 'mouse', 'monitor', 'computer', 'pendrive']

print(products)

products[1] = 'smart-printer'

print(products)

a = ['smart-mouse','LED-monitor']

products[2:4] = a

print(products)

## insert item
print("=====insert items====",end='\n\n')

products = ['smartphone', 'printer', 'mouse', 'monitor', 'computer', 'pendrive']

print(products)

products.insert(3,"LED")

print(products)

products.insert(3,["LED","headphone"])

print(products)

# example of list inside list (nested list)
# emp_record = [
#     ['1','Aman','DevOps','3.5 yrs'],
#     ['2', 'Karthik', 'Devops' , '22 yrs'],
# ]


##### 

print("=====append items====",end='\n\n')

products = ['smartphone', 'printer', 'mouse', 'monitor', 'computer', 'pendrive']

print(products)

another_products = 'headphone'

products.append(another_products)

print(products)

## remove from list 

print("=====remove items====",end='\n\n')

products = ['smartphone', 'printer', 'mouse', 'monitor', 'computer', 'pendrive','mouse']

print(products)

products.remove("mouse")

products.remove("mouse")

print(products)

products.pop(4)

print(products)

products.clear()

print(products)


##### copy list 
print("=====copy items====",end='\n\n')


products = ['smartphone', 'printer', 'mouse', 'monitor', 'computer', 'pendrive']

products_bkp = products

# products_bkp = products, here product_bkp is a reference to product, 
# so if we do any change in product it will reflect in product_bkp 

# note : products_bkp = products , this shouldn't be used to copy the list

print(products)

print(products_bkp)

products.pop(3)

print(products)

print(products_bkp)


### then what we use for copy list to another list 

products = ['smartphone', 'printer', 'mouse', 'monitor', 'computer', 'pendrive']

products_bkp = products.copy()

products.pop(3)

print(products)

print(products_bkp)


### join list

print("=====join items====",end='\n\n')

product = ['smartphone', 'printer', 'mouse', 'monitor', 'computer', 'pendrive']

another_products = ['headphone','LED']

product =  product + another_products

print(product)