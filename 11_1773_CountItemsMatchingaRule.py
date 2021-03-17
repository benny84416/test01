# items[i] = [typei, colori, namei]
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
## Ex:
# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], 
# ruleKey = "color"
# ruleValue = "silver"
# Output = 1 #["computer","silver","lenovo"]

# def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str)
# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = "color"
# ruleValue = "silver"

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

# Solution 1

# rule = {"type":0,"color":1,"name":2}
# # print(rule.get("type"))
# count = 0
# for value in items:
#     if value[rule.get(ruleKey)] == ruleValue:
#         # print(n)
#         count+=1
# print(count)

# Solution 2

if ruleKey == "type":
    n = 0
elif ruleKey == "color":
    n = 1
elif ruleKey == "name":
    n = 2
count = 0
for value in items:
    if value[n] == ruleValue:
        count+=1
print(count)     
