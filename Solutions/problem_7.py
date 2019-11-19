# # By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# # What is the 10 001st prime number?

import math
def isprime(num):
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if num % i == 0:
            return False
    return True

n = 1
count = 1
while(count != 10001):
    n += 2
    if isprime(n):
        count += 1
print(n)
