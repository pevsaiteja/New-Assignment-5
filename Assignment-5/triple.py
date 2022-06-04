number = [8,9,10,12,16,18,19,20]
print("Original list:", number)
result = map(lambda x: x + x + x ,number)
print("\nTriple of the given list numbers:")
print(list(result)) 