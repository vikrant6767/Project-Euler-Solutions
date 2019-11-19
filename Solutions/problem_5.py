# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 2520
x = 0
check = False
li = [19, 18, 17, 16, 15, 14, 13, 12, 11]
while(check==False):
    check = True
    for i in li:
        if n % i != 0:
            check = False
            break
    if check == True:
        print(n)
    n += 20