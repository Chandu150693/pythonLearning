import re

text = "Cat cup carrot dog"

pattern = re.compile(r'\bc', re.IGNORECASE)
matches = pattern.findall(text)

print(matches)


txt = "The rAin in Spain"
x = re.search("ai", txt)
print(x)
print(x.span())


txt = "The rain in Spain"
x = re.search("in", txt)
print("The ele is located at : ", x.start())
