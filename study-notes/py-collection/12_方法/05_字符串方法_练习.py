while True:
    print('回复：' +
          input('提问：')
          .replace('你', '朕')
          .replace('么', '')
          .replace('吗', '')
          .replace('麽', '')
          .replace('？', '！')
          .replace('?', '!')
          )

# 链式编程

# while True:
#     s = input('提问：')
#     s = s.replace('你', '朕')
#     s = s.replace('么', '')
#     s = s.replace('吗', '')
#     s = s.replace('麽', '')
#     s = s.replace('？', '！')
#     s = s.replace('?', '!')
#     print('回复：' + s)
