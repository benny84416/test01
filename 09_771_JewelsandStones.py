# J,S中每個值各表是一種類別(ex. J=a,A S=a,A,b)，找出J在S裡相同的類別數量
# Input: J = "aA", S = "aAAbbbb"
# Output: 3


count=0
for m in S:
    if m in list(J):
        count+=1
print(count)