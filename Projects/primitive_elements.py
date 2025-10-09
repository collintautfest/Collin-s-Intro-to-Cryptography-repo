'''
Author: Collin Tautfest
Date: 2025-10-09

Project: Modtabs Primitive elements
'''
import math

def is_prime(x):
    """
    checks if a element is prime
    """
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# Helper: check if n = p^k for some prime p
def is_prime_power(n, require_odd=False):
    # Try every possible prime base up to sqrt(n)
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0 and is_prime(p):
            if require_odd and p == 2:
                continue  # skip even prime if we need odd only

            m = n
            # Divide out all factors of p
            while m % p == 0:
                m //= p

            # If we reduced all the way to 1, it's a perfect prime power
            if m == 1:
                return True

    # Special case: n itself is prime (p^1)
    if is_prime(n):
        if require_odd and n == 2:
            return False
        return True

    return False



def get_primitive_elements(n):
    # check if n is in set {2, 4, p^k or 2p^k} where p is a prime number
    if n in {2, 4} or is_prime_power(n) or (n % 2 == 0 and is_prime_power(n // 2, require_odd=True)):
        print()


    else:
        # if not in set it cannot have primitves
        print("No primitives for Z_", n)

def main():
    """
    main function of program, will include multiple menu options in final version
    """

    x = 23 # placeholder number for input

    get_primitive_elements(x) # call primitive function


if __name__ == "__main__":
    main()