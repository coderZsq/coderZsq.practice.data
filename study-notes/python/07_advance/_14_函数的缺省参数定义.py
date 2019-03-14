def print_info(name, gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


print_info("小明")
print_info("老王")
print_info("小美", False)
