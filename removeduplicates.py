
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

print("List without duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
