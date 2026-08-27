
def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

print("Is 28 a perfect number?", is_perfect(28))
print("Is 12 a perfect number?", is_perfect(12))
