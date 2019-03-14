import os
import multiprocessing


def copy_file(file_name, old_folder_name, new_folder_name):
    print("======>模拟copy文件: 从%s--->到%s 文件名是:%s" % (old_folder_name, new_folder_name, file_name))
    open(old_folder_name + "/" + file_name, "rb")
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()
    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()


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
    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name))
    po.close()
    po.join()


if __name__ == '__main__':
    main()