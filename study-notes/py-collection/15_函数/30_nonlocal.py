def test3():
    k = 10

    def test4():
        k = 200
        def test5():
            nonlocal k
            k = 40
        test5()

    print(f'k={k}')
    test4()
    print(f'k={k}')


test3()

# k = 10
#
#
# def test3():
#     def test4():
#         def test5():
#             nonlocal k
#             k = 40
#         test5()
#     test4()
#
#
# print(f'k={k}')
# test3()
# print(f'k={k}')
