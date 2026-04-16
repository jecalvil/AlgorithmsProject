import math

### Checker Functions

# function takes in value of n, and checks all numbers from 2 to the square root
# of n and finds any factors to determine if prime
# Time Complexity O(sqrt(n))
def trialDivisionCheck(n):
    # negative numbers and 1 are not considered prime
    if n < 2:
        return False
    
    # our upper limit of where we have to check
    wall = int(math.sqrt(n))

    # check every value from 2 to wall, if it divides, then it is not prime since factor was found
    for i in range(2, wall + 1):
        if n % i == 0:
            return False # found factor -> not prime
    return True # no factor found -> prime

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

### Generator Functions

# function using brute force by finding prime numbers up to a specified range and returns a list of prime numbers found
# Time Complexity O(n * sqrt(n))
def trialDivisionGenerator(n):
    # prime numbers
    primes = []
    for number in range(2, n + 1):
        # Use trialDivisionCheck to determine if prime
        if trialDivisionCheck(number):
            primes.append(number)
    return primes

# Sieve of Eratosthenes
# Time Complexity: O(nloglogn)
def sieveOfEratosthenes(n):
    # create list of n + 1 true values, index represents our numbers
    isPrime = [True] * (n + 1)
    
    # 0 and 1 are automatically not prime
    isPrime[0] = False
    isPrime[1] = False

    # Go from 2 to square root of n
    wall = int(math.sqrt(n))
    for i in range(2, wall + 1):
        if isPrime[i]:
            # start at i * i, to n + 1, step of a multiple of i
            for j in range(i * i, n + 1, i):
                isPrime[j] = False

    # list comprehesion - create new list of just the prime numbers
    primeValues = [number for number in range(n + 1) if isPrime[number]]

    # return the prime numbers
    return primeValues
