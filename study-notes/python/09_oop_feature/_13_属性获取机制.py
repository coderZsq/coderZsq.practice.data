class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# print(Tool.count)
print("工具对象总数 %d" % tool3.count)
