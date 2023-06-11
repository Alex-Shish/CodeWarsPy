# DESCRIPTION:
# Define a function that takes an integer argument and returns a logical value true or false depending on
# if the integer is a prime.
# Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors
# other than 1 and itself.
# Requirements
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
# NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out.
# Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.

def is_prime(n):
    if n <= 0 or n == 1:
        return False
    if n == 2:
        return True
    i = 2
    while (i <= n ** 0.5 + 1):
        if n % i == 0:
            return False
        i += 1
    return True


print(is_prime(0))
print(is_prime(-25))
print(is_prime(13))
print(is_prime(75))
print(is_prime(73))
