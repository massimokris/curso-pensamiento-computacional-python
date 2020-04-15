def factorial(n):
    """Calculate the factorial of n

    n int > 0
    returns n!
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input('Write a number: '))

print(factorial(n))