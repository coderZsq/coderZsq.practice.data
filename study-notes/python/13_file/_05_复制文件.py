file_read = open("README")
file_write = open("README[复件]", "w")

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()
