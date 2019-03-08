#!/usr/bin/env python3

primes = [2]
for number in range(3,100):
    is_prime = 0
    for prime in primes:
        if number % prime == 0:
            break
        else:
            is_prime = 1
    if is_prime:
        primes.append(number)
    if len(primes) >= 10:
        print(primes);
        break
