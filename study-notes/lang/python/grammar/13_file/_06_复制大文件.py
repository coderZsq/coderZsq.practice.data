file_read = open("README")
file_write = open("README[复件]", "w")

while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)

file_read.close()
file_write.close()
