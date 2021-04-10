# Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
# array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].

# Input: encoded = [1,2,3], first = 1
# Output: [1,0,2,1]

# Input: encoded = [6,2,7,3], first = 4
# Output: [4,2,0,7,4]

## XOR = ^
##[1^0,0^2,2^1] = [1,2,3]
# a ^ b = c  
# c ^ b = a

encoded = [6,2,7,3]
first = 4

arr = [first]

for n in range(len(encoded)):

    arr.append(encoded[n] ^ arr[n])
print(arr)


 
