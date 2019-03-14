file = open("README")

text = file.read()
print(text)
print(len(text))

print("-" * 50)

text = file.read()
print(text)
print(len(text))

file.close()
