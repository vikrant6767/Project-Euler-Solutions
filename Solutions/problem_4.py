# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def check_palindrome(num):
    temp = num
    sum = 0
    while(temp > 0):
        last_digit = temp % 10
        sum = sum * 10 + last_digit
        temp = int(temp / 10)
    if num == sum:
        return True
    else:
        return False

def largest_palindrome():
    palindromes = 0
    for i in range(999, 1, -1):
        if palindromes != 0:
            break
        for j in range(999, 1, -1):
            if check_palindrome(i*j):
                palindromes = i*j
            break
    print(palindromes)

largest_palindrome()

