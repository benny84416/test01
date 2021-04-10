# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

# n = 234
n = 705
Sum = 0
Product = 1
List = list(str(n))
for s in List:
    # print(s)
    Sum+=int(s)
    Product*=int(s)
# print(Sum)
# print(Product)
print(Product - Sum)