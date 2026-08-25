
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print("Fibonacci sequence (first 10 numbers):", fibonacci(10))
