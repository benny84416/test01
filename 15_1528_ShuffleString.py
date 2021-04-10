# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

s = "aiohn"
indices = [3,1,4,2,0]
# Output: "nihao"

# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]

# Solution 1

dic = {}  
result = ""
for n,m in enumerate(indices):
    dic[m] = s[n]
# print(dic)
for x in range(len(indices)):
    result += dic[x]
print (result)

# Solution 2

List = list(s)
for n,m in enumerate(indices):
    List[m] = s[n]
# print(List)
print(''.join(List))
