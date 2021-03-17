# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]

nums = [1,2,3,4]

b=[]
a=0
for i in nums:
    a+=i
    b += [a]
print(b)
