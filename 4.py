### Tuple ###

## Tuple :- -> ordered, unchangable, and value can be duplicated 

products = ('smartphone', 'printer', 'mouse', 'monitor', 'computer')

print(products)

#### 

print(products[0])

print(products[-1])

print(products[1:3])


### update 


products_tuple = ('smartphone', 'printer', 'mouse', 'monitor', 'computer')

print(products_tuple)


## coverting tuple to list
products_list = list(products_tuple)

## update the list
products_list[1] = 'headphone'

print(products_list)

## converting list back to tuple
products_tuple = tuple(products_list)

print(products_tuple)

## Append Items

products_tuple = ('smartphone', 'printer', 'mouse', 'monitor', 'computer')

print(products_tuple)


## coverting tuple to list
products_list = list(products_tuple)

## append the list
products_list.append('headphone')

print(products_list)

## converting list back to tuple
products_tuple = tuple(products_list)

print(products_tuple)

## to do's

## assign tuple items to multiple Variables


## join 

products_1 = ('smartphone', 'printer', 'mouse', 'monitor', 'computer')

products_2 = ('headphone', 'LED')

products_3 = products_1 + products_2

print(products_3)

products_4 = products_2 * 2

print(products_4)

### 

print(products_4.count('headphone'))

print(products_2)

products_2 = set(products_2)

print(products_2)






