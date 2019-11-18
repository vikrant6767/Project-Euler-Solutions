# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def prime(num):
    f = []
    while(num > 1):
        for x in range(2, num + 1):
            if num % x == 0:
                f.append(x)
                num = int(num/x)
                break
    print(max(f))

prime(600851475143)