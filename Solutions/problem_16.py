# 2(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2(1000)?


def digit_sum(num):
    sum = 0
    while(num > 0):
        mod = int(num % 10)
        sum += mod
        num = num // 10
    return sum
n = 2 ** 1000
print(digit_sum(n))
