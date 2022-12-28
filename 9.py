
############# while loops

print("#####################", end="\n\n")

print("Example-1")

speed = 0

while speed <= 30:
    print(speed)
    speed+=2




### continue 

print("#####################", end="\n\n")

print("Example-2")

speed = 0

while speed <= 15:
    if speed == 8:
        speed+=2
        continue
    print(speed)
    speed+=2

### continue 

print("#####################", end="\n\n")

print("Example-3")

speed = 0

while speed <= 15:
    if speed == 8:
        break
    print(speed)
    speed+=2

#### while with else 


print("#####################", end="\n\n")

print("Example-4")

speed = 0

while speed <= 15:
    print(speed)
    speed+=2
else:
    print('loop completed at :',speed)

