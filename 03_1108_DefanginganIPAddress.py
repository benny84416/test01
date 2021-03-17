# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

address = "1.1.1.1"

# a = address.replace('.','[.]')

a = '[.]'.join(address.split('.'))

print(a)