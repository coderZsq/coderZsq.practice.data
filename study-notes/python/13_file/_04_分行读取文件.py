file = open("README")

while True:
    text = file.readline()
    if not text:
        break
    print(text)

file.close()