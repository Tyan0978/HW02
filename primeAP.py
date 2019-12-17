# find arithmetic sequences in [a,b)

def find_prime_AP(a,b):

    # find primes in [a,b)

    is_primes = [i for i in range(a,b)]
    for n in range(a,b):
        if n < 2:
            is_primes.remove(n)
            continue

        i = 2
        while i <= n**(0.5):
            if n % i == 0 or n == 1:
                is_primes.remove(n)
                break
            i += 1

    return(is_primes)

if __name__ == '__main__':
    primes = find_prime_AP(1,20)
    print(primes)
