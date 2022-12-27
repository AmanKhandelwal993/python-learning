### loops 

### for loops 

## to run loop for n number of times 

# for i in range(n):
#     print(i)

from email import contentmanager


print("Example-1")

print("Running loop for 6 times")

for i in range(6):
    print(i)


############# print counting from 1 to 10

print("#####################", end="\n\n")

print("Example-2")

n = 10
# count = 0
for i in range(n):
    # count = count + 1
    i+=1
    print(i)
    # print(count)


# output :- 

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10



########
print("#####################", end="\n\n")

print("Example-3")

product = ['erp','cms','hr','admin']

####
# erp -> financials system 
# cms -> content management
# hr -> human resources

count=0
for i in product:
    if i == 'erp':
        print('financials system ')
    elif i == 'cms':
        print('content management')
    elif i == 'hr':
        print('human resources')
    else:
        print('wrong input')
    count=count+1

print(count)


##### countinue :- bring cursor to top of the loops.

print("#####################", end="\n\n")

print("Example-4")

product = ['erp','admin','cms','hr','erp','IT','hr']

count=0
for i in product:
    print('starting loop cycle')
    if i == 'erp':
        print('financials system ')
    elif i == 'cms':
        print('content management')
    elif i == 'hr':
        print('human resources')
    else:
        print('wrong input',end='\n\n')
        continue
    count=count+1
    print('ending loop cycle',end='\n\n')

print("Count")
print(count)


##### break : - comes out of the loops 

print("#####################", end="\n\n")

print("Example-4")

product = ['erp','cms','hr','erp','IT','hr']

count=0
for i in product:
    print('starting loop cycle')
    if i == 'erp':
        print('financials system ')
    elif i == 'cms':
        print('content management')
    elif i == 'hr':
        print('human resources')
    else:
        print('wrong input',end='\n\n')
        break
    count=count+1
    print('ending loop cycle',end='\n\n')

print("Count")
print(count)
