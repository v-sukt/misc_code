primes = [2]
for number in range(3, 100000):
    is_prime = 0
    for prime in primes:
        if number % prime == 0:
            break
        else:
            is_prime = 1
    if is_prime:
        primes.append(number)
    # if len(primes) >= 10:
        # print(primes);
        # break
print(primes)
"""
real    0m25.339s
user    0m25.131s
sys     0m0.010s
"""
