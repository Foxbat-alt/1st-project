def sum_of_multiples(limit):
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)

result = sum_of_multiples(1000)
print("Sum of multiples of 3 or 5 below 1000:", result)

def sum_even_fibonacci(limit):
    a, b = 1, 2  # Starting terms
    total = 0
    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

# Call the function with the 4 million limit
result = sum_even_fibonacci(4_000_000)
print(result)

def largest_prime_factor(n: int) -> int:
    # Remove factors of 2
    last = 1
    while n % 2 == 0:
        last = 2
        n //= 2

    # Test odd factors from 3 upward
    f = 3
    while f * f <= n:
        if n % f == 0:
            last = f
            while n % f == 0:
                n //= f
        f += 2

    # If remaining n > 1 it's prime and the largest factor
    if n > 1:
        last = n
    return int(last)

if __name__ == "__main__":
    target = 600851475143
    print(largest_prime_factor(target))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a  
def lcm(a, b):
    return a * b // gcd(a, b)  
def lcm_multiple(numbers):
    from functools import reduce
    return reduce(lcm, numbers) 
if __name__ == "__main__":
    numbers = range(1, 21)
    print(lcm_multiple(numbers))    
def sum_square_difference(n):
    sum_of_squares = sum(i * i for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    return square_of_sum - sum_of_squares
print(sum_square_difference(100))  # Output: 25164150
def nth_prime(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    count = 0
    candidate = 1
    
    while count < n:
        candidate += 1
        for i in range(2, int(candidate**0.5) + 1):
            if candidate % i == 0:
                break
        else:
            count += 1
            
    return candidate
print(nth_prime(10001))  # Output: 104743
def print_christmas_tree(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))
    print(' ' * (height - 1) + '|')

import math
import time

def count_divisors(n: int) -> int:
    """Return number of divisors of n by prime factorization via trial division."""
    if n <= 1:
        return 1
    count = 1
    x = n

    # factor out 2
    exp = 0
    while x % 2 == 0:
        x //= 2
        exp += 1
    if exp:
        count *= (exp + 1)

    # factor odd numbers
    f = 3
    limit = int(math.isqrt(x)) + 1
    while f <= limit and x > 1:
        exp = 0
        while x % f == 0:
            x //= f
            exp += 1
            limit = int(math.isqrt(x)) + 1
        if exp:
            count *= (exp + 1)
        f += 2

    # if remainder is a prime
    if x > 1:
        count *= 2

    return count

def first_triangle_with_over_divisors(target_divisors: int = 500) -> int:
    """Return the first triangle number that has more than target_divisors divisors."""
    k = 1
    while True:
        # triangle number T_k = k*(k+1)//2
        # since gcd(k, k+1) == 1, compute divisors of k and k+1 separately,
        # but divide the even one by 2 to account for the /2 in T_k.
        if k % 2 == 0:
            a = k // 2
            b = k + 1
        else:
            a = k
            b = (k + 1) // 2

        divisors = count_divisors(a) * count_divisors(b)
        if divisors > target_divisors:
            return k * (k + 1) // 2
        k += 1

if __name__ == "__main__":
    start = time.time()
    result = first_triangle_with_over_divisors(500)
    elapsed = time.time() - start
    print("First triangle number with over 500 divisors:", result)
    print("Elapsed: {:.3f} s".format(elapsed))
    

