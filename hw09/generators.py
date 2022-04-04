
### simple generators.

def gen_primes():
    yield 2
    yield 3
    yield 5
    yield 7
    yield 11

def gen_naturals():
    n = 0
    while True:
        yield n
        n += 1
