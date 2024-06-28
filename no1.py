import itertools
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def extract_primes(num):
    num_str = str(num)
    primes = set()
    
    
    for length in range(1, len(num_str) + 1):
        for sub in itertools.permutations(num_str, length):
            candidate = int(''.join(sub))
            if is_prime(candidate):
                primes.add(candidate)
    
    return sorted(primes)

a= input()
output = extract_primes(a)
print(output)