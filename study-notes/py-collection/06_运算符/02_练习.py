# 提示输入信息
n = int(input('请输入秒数：'))

# 计算出对应的分、秒，比如500秒 == 8分20秒
# 500 == 60 * 8 + 20
minute = n // 60
second = n % 60

print(f'{n}秒等于{minute}分{second}秒')
