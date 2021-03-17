#Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.


# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
# allowed = "abc"
# words = ["a","b","c","ab","ac","bc","abc"]

allowed = "fstqyienx"
words = ["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"]

# print(type(a))
# print(words[2][3])
count = 0
for word in words:
    # print(list(word))
    for w in word:
        if w not in list(allowed):
            # print(word)
            count+=1
            break  ###非常重要  發現一個不相符，自動跳下一個 不然同一個單字有兩個不相符會重複累加
# print((count))
print(len(words)-count)