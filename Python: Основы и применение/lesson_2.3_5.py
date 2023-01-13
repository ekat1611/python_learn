import itertools


def primes():
    i = 1
    while i:
        i += 1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


print(list(itertools.takewhile(lambda x : x <= 31, primes())))