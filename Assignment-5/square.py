def square_num(n):
 return n * n
number = [6,7,4,9,5]
print ("Original list to squared:",number)
result = map(square_num, number)
print("Square thr numbers in the given list using map():")
print(list(result))
 