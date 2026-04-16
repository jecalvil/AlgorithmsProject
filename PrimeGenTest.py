import math
import random

# Trial Division Prime Generator
def generate_primes_trial_division(limit):
    """
    Generate all prime numbers up to 'limit' using trial division.

    Precondition:
        limit is an integer >= 2
    Postcondition:
        returns a list of all primes <= limit
    """
    if limit < 2:
        return []

    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(math.sqrt(num)) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Miller-Rabin Primality Tester
def is_prime_miller_rabin(n, k=10):
    """
    Probabilistic primality test using Miller-Rabin.

    Precondition:
        n is an integer
        k is the number of test rounds
    Postcondition:
        returns True if n is probably prime, otherwise False

    Note:
        More rounds (k) means higher confidence.
    """
    if n < 2:
        return False

    # Small prime checks
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0 and n != p:
            return False

    # Write n - 1 as d * 2^r
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        passed_round = False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                passed_round = True
                break

        if not passed_round:
            return False

    return True

# Example usage
if __name__ == '__main__':
    # Generate primes up to 50 using trial division
    primes = generate_primes_trial_division(50)
    print("Primes up to 50:", primes)

    # Test some numbers with Miller-Rabin
    test_numbers = [97, 221, 997, 10007]
    for num in test_numbers:
        result = is_prime_miller_rabin(num)
        print(f"{num} is prime? - {result}")
