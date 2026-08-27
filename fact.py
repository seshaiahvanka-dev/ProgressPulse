
def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print("Factorial of 6 is:", factorial_iterative(6))
