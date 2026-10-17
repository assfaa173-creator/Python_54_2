import re

text = "The status is passed"
result = re.search("passed",text)
print(result)
#print(result.group())

text2 = "passed: test registration"
text3 = "test registration: passed"
print(re.match("Passed",text2))
print(re.match("passed",text3))

print(re.match("Passed: test registration",text2))
print(re.match("Passed: test registration ",text2))
print()

print(re.search("d.g","dog"))
print(re.search("d.g","dig"))
print(re.search("d..g","dg"))
print(re.search("d..g","doog"))

order = "ORD-12345"
assert re.fullmatch(order,"ORD-12345")
print(re.fullmatch("ORD-12345",order))

print(re.search("^Test","Test is start"))
print(re.search("^Test","Start is test"))

print(re.search("Test$","start is Test"))
print(re.search("Test$","test is start"))
