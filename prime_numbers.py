def generate_primes(n):
    primes = []
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

# Example usage:
number = int(input("Enter a number: "))
result = generate_primes(number)
print(f"Prime numbers smaller than {number}:")
print(result)
