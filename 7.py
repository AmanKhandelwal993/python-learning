## condtional statements

##
# if <condtions-1> :
#     <statement-1>
# elif <conditon - 2> :
#     <statement -2> 
# else :
#     <statement-n>

print("Example-1")

condition = 2

if condition == 1:
    print("Condition 1 Ran")
elif condition == 2:
    print("Condition 2 Ran")
else:
    print("No Condition Ran")


#####################

print("#####################", end="\n\n")

print("Example-2")

speed = 0

# lower 40
# 40-80
# 80 and above

if speed <= 40 and speed >= 0:
    print("low speed")
elif speed > 40 and speed <= 80:
    print("medium speeed")
elif speed > 80:
    print("high speed")
else:
    print("Wrong Input")


#######  taking iterable as

print("#####################", end="\n\n")

print("Example-3")

product = ['erp','cms','hr']

if "hr" in product:
    print("Success")

if "finance" not in product:
    print("Success")

## to check subset of a particular string

output = "this test is a Success"

if "success" in output.lower():
    print("yes I do have success keyword in output string")


########
