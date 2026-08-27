
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

print("Sum of digits of 12345 is:", sum_of_digits(12345))
