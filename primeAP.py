# find arithmetic sequences in [a,b)

def find_prime_AP(a,b):

    # find primes in [a,b)

    primes = [i for i in range(a,b)]
    for n in range(a,b):
        if n < 2:
            primes.remove(n)
            continue

        i = 2
        while i <= n**(0.5):
            if n % i == 0 or n == 1:
                primes.remove(n)
                break
            i += 1

    # find sequences

    prime_AP = []

    for i in primes:
        for j in primes:
            if j <= i:
                continue

            d = j - i
            last_n = j + d
            seq_ap = [i, j]
            while last_n in primes:
                seq_ap.append(last_n)
                last_n += d

            if len(seq_ap) > 2:
                prime_AP.append(seq_ap)

    return prime_AP

if __name__ == '__main__':
    primeAPs = find_prime_AP(1,40)
    print(primeAPs)
