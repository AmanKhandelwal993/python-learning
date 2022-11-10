## sets 

# sets :- unordered, not allow duplicates, unchangable

from math import prod


products_1 = {'smartphone', 'printer', 'mouse', 'monitor', 'computer'}

products_2 = {'smartphone', 'headphone', 'LED'}

print(products_1.intersection(products_2))

print(products_1.difference(products_2))

print(products_1.union(products_2))

products_1 = list(products_1)

print(products_1)


### add into set

products_1 = {'smartphone', 'printer', 'mouse', 'monitor', 'computer'}

products_1.add('headphone')

print(products_1)

products_1.add('smartphone')

print(products_1)

## for joining the sets

print(products_1.union(products_2))


products_1 = {'smartphone', 'printer', 'mouse', 'monitor', 'computer'}

print(products_1)

products_1.update(('headphone','LED'))

print(products_1)