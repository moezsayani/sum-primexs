def primes_sieve(limit):
    primes = []
    limitn = limit + 1
    not_prime = [False] * limitn
    for i in range (2, limitn):
        if not_prime[i]:
            continue
        for j in range(i*2, limitn, i):
            not_prime[j] = True
        primes.append(i)
    return primes
print(sum(primes_sieve(110)))
