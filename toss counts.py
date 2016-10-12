import random
heads = 0
tails = 0

for i in range(0,100):
    flip = random.randint(0,1)
    print(flip)
    if flip == 0:
        heads +=1
    else:
        flip ==1
        tails +=1

print("heads count%i." %heads)
print("tails count%i." %tails)
