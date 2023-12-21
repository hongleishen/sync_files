import numpy as np
import sys
import os

def test_os_walk(dir):
    print("dir = ", dir)

    #  遍历到的路径          当前路径下的file
    #           当前路径下 dir
    for dirpath, dirnames, filenames in os.walk(dir):
        # 打印当前目录路径
        print(f'Found directory: {dirpath}')
        
        # 打印当前目录下的所有子目录
        if dirnames:
            print("     Subdirectories:")
            for dirname in dirnames:
                print(f'\t\t {dirname}')

        # 打印当前目录下的所有文件
        if filenames:
            print("     Files:")

            for filename in filenames:
                print(f'\t\t {filename}')
                file_path = os.path.join(dirpath, filename)
                print("\t\t file_path = ", file_path)
        print("\n")





def read_dir(dir):
    text = ''
    for root, dirs, files in os.walk(dir):  
        print('the path is ...')
        print(root)  
        print('the current directories under current directory :')
        print(dirs)  
        print('the files in current directory :')
        print(files)
        print('')

        for file in files:
            d = root + '\\' + file
            print('reading dir', d)
            fin = open(d, encoding="utf-8")
            input_file = fin.read()
            fin.close()
            #print(input_file)
            text += input_file + '\n'

    return text


def os_walk_add_dmesg_(dir):
    print("dir = ", dir)

    for dirpath, dirnames, filenames in os.walk(dir):
        # 打印当前目录路径
        print(f'Found directory: {dirpath}')

        print(f" before skip_dirs = {dirnames}")
        dirnames = [d for d in dirnames if d not in skip_dirs]
        print(f" after skip_dirs = {dirnames}")

        # 打印当前目录下的所有子目录
        if dirnames:
            print("     Subdirectories:")
            for dirname in dirnames:
                print(f'\t\t {dirname}')

        # 打印当前目录下的所有文件
        if filenames:
            print("     Files:")

            for filename in filenames:
                print(f'\t\t {filename}')
                file_path = os.path.join(dirpath, filename)
                print("\t\t file_path = ", file_path)
        print("\n")



def os_walk_add_dmesg(dir):
    for dirpath, dirnames, filenames in os.walk(dir):
        # a. 打印当前目录路径
        print(f'正在遍历路径: {dirpath}')

        if dirpath in skip_dirs:
            print("skip dirpath", dirpath)
            continue

        #       1. 打印当前目录下的所有子目录
        if dirnames:
            print("     遍历到的路径下的子目录名:")
            for dirname in dirnames:
                print(f'\t\t {dirname}')

        #       2. 打印当前目录下的所有文件
        if filenames:
            print("     Files:")

            for filename in filenames:
                print(f'\t\t {filename}')
                file_path = os.path.join(dirpath, filename)
                print("\t\t file_path = ", file_path)
        print("\n")


if __name__ == '__main__':
    skip_dirs = ['00_c_code\simple\dir_b', 'dir_a']
    #fin = open("2.c", encoding="utf-8")
    #input_file = fin.read()
    #fin.close()

    if len(sys.argv) >= 2:
        dir = sys.argv[1]
    else:
        dir = '.\\'

    #input_files = read_dir(dir)
    test_os_walk(sys.argv[1])
    print("\n\n============================")
    os_walk_add_dmesg(sys.argv[1])