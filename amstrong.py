
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(d)**power for d in digits)

print("Is 153 an Armstrong number?", is_armstrong(153))
print("Is 9474 an Armstrong number?", is_armstrong(9474))
