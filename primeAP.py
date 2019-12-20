# find arithmetic sequences in [a,b)

def find_prime_AP(a,b):

    # find primes in [a,b)

    if type(a) == float:
        a = int(a+1)
    if type(b) == float:
        b = int(b+1)

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
    exist_seq = {}
    longest_len = 0
    for i in primes:
        for j in primes:
            if j <= i:
                continue

            d = j - i
            last_n = j + d
            seq_ap = [i, j]
            if not d in exist_seq:
                exist_seq[d] = []

            if i in exist_seq[d]:
                continue

            while last_n in primes:
                seq_ap.append(last_n)
                exist_seq[d].append(last_n)
                last_n += d
            else:
                exist_seq[d].append(i)
                exist_seq[d].append(j)

            if len(seq_ap) > 2:
                prime_AP.append(seq_ap)
                if len(seq_ap) > longest_len:
                    longest_len = len(seq_ap)

    longest_seq = []
    for seq in prime_AP:
        if len(seq) == longest_len:
            longest_seq.append(seq)

    return longest_seq

if __name__ == '__main__':
    primeAPs = find_prime_AP(1,40)
    print(primeAPs)
