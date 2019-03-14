#! /usr/local/bin/python3.6

import cards_tools

while True:
    # TODO(Castie!) 需要做的功能
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作: ")
    print("您选择的操作是[%s]" % action_str)

    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools.new_card()
            pass
        elif action_str == "2":
            cards_tools.show_all()
            pass
        elif action_str == "3":
            cards_tools.search_card()
            pass
    elif action_str == "0":
        print("欢迎再次使用[名片管理系统]")
        break
        pass
    else:
        print("您输入的不正确, 请重新选择")