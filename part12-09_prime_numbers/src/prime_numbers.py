def prime_numbers():
    primes = []
    n = 2
    while True:
        for prime in primes:
            if n % prime == 0:
                break
        else:
            primes.append(n)
            yield n
        n += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
