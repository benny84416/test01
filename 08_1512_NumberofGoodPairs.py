# Given an array of integers nums.
#
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#
# Return the number of good pairs.

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# i,j是兩變數，算出nums數組中的值(i,j)符合 if nums[i] == nums[j] and i < j 這條件的組合(i,j)有多少個

count=0
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] == nums[j] and i < j:
#             print(i,j)
            count+=1
print(count)









