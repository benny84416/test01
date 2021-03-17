# TwoSum  找出list中兩個相加等於target的位置 list[a]+list[b]=target print[a,b]

nums = [2,7,11,15]
target = 9

#Solution 1

# d = {}
# for i, num in enumerate(nums):
#
#     if num in d:
#         print([d[num], i])
#     else:
#         d[target - num] = i

# Solution 2

d={}
for a in range(len(nums)): #取出list 所有值的位置
    # print(a)
    b = target-nums[a]
    if b in d:
        print([d[b],a])
    else: #如果b值不再字典d中 建立nums[a]的位置字典
        d[nums[a]] = a


