def get_factors(n, i=1, factors=None):
    if factors is None:
        factors = []

    if i > n:
        return factors

    if n % i == 0:
        factors.append(i)

    return get_factors(n, i + 1, factors)

number = 12
result = get_factors(number)

print(f"The factors of {number} are: {result}")
