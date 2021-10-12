# 将小说的主要人物记录在文件中
file1 = open('name.txt', 'w')
file1.write('诸葛亮')
file1.close()

file2 = open('name.txt')
print(file2.read())

file2.close()

file3 = open('name.txt', 'a')
file3.write('刘备')
file3.close()