# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6

accounts =  [[2,8,7],[7,1,3],[1,9,5]]
l=[]
for n in accounts:
    l+=[sum(n)]
print(max(l))