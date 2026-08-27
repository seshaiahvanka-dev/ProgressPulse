
def second_largest(numbers):
    unique_nums = list(set(numbers))
    unique_nums.sort(reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None

print("Second largest number:", second_largest([10, 25, 7, 99, 42]))
