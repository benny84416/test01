# Example 1:

# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
# Constraints:

# 2 <= nums.length <= 100
# nums.length % 2 == 0
# 1 <= nums[i] <= 100

nums = [1,2,3,4]

# Solution 1
List = []
for i,m in enumerate(nums):
    if i%2 == 0:
        List.extend(m*[nums[i+1]]) # extend 放入同一個List
print(Listr)

# Solution 2
List = []
for i in range(0,len(nums),2):
    # print([nums[i]])
    # print(nums[i]*[nums[i+1]])
    List.extend(nums[i]*[nums[i+1]])

print(List)

