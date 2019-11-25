# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

terms = dict()
limit = 1000000

def chain_number(number):
    if number in terms:
        return terms[number]
    if number == 1:
        return 1
    if number%2==0:
        numberTerms = chain_number(number//2) + 1
    else:
        numberTerms = chain_number(number*3 + 1) + 1
    if number < limit:
        terms[number] = numberTerms
    return numberTerms

maxCount = 1
maxTerms = 1
for number in range(limit//2, limit):
    currentTerms = chain_number(number)
    if currentTerms > maxTerms:
        maxTerms = currentTerms
        maxCount = number

print(maxCount, maxTerms)
