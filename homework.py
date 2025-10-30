import random
sum=0
for i in range(10000001):
    x=random.randint(1,6)
    y=random.randint(1,6)
    if x+y==7:
        sum+=1
print(f"The probability of getting the number 7 {sum / 10000000}")