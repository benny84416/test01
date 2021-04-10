
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# 比8小的數字有4個，比1小有0個，比2小有1個，以此類推。


nums = [8,1,2,2,3]

List = []
for n in nums:
    count = 0
    for m in nums:
        if n > m :
            # print(n,m)
            count+=1
    # print(count)
    List.append(count)
return List
