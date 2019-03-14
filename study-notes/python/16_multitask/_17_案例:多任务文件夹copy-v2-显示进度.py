import os
import multiprocessing


def copy_file(q, file_name, old_folder_name, new_folder_name):
    print("======>模拟copy文件: 从%s--->到%s 文件名是:%s" % (old_folder_name, new_folder_name, file_name))
    open(old_folder_name + "/" + file_name, "rb")
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()
    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()
    q.put(file_name)


def main():
    old_folder_name = input("请输入要copy的文件夹名字")
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass
    file_names = os.listdir(old_folder_name)
    print(file_names)
    po = multiprocessing.Pool(5)
    q = multiprocessing.Manager().Queue()
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))
    po.close()
    # po.join()
    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        print("已经完成copy: %s" % file_name)
        copy_ok_num += 1
        print("\r拷贝的进度为: %.2f %%" % (copy_ok_num * 100/ all_file_num), end="")
        if copy_ok_num >= all_file_num:
            break
    print()


if __name__ == '__main__':
    main()