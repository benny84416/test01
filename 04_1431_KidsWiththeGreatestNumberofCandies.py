# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]

candies = [2,3,5,1,3]
extraCandies = 3

l =[]
for n in candies:
    l+=[n+extraCandies >= max(candies)]
print(l)

