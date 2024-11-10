def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)  # Alternatively, you could use set1 ^ set2

# Example usage
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
result = symmetric_difference(set_1, set_2)
print("Symmetric Difference:", result)
