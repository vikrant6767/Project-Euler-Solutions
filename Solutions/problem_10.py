# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def prime_list(n):
    not_prime = set()
    for i in range(2, n+1):
        if i not in not_prime:
            yield i #then its prime
            #Add multiples of the prime in the range to the 'invalid' set
            not_prime.update(range(i*i, n+1, i))

print(sum(list(prime_list(2000000))))