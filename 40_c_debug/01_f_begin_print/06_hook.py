import numpy as np
import sys
import os
import re



def  process_text(text):
    in_lines = text.split("\n")    
    ff1 = 0         # find func (
    ff2 = 0         # find func )
    ff3 = 0         # fidn func {
    ff_end = 1      # find func }
    out_text = ''
    lcommit_start = 0
    next_line_skip = 0

    '''
    for index, element in enumerate(in_lines):
        print(f"index = {index}: {element}")
    '''

    for index, line in enumerate(in_lines, start=1):
       
        if not (ff1 and ff2 and ff3 and line.startswith("}")):
            out_text += line + '\n'
            
        if line.startswith("/*") or line.startswith("*") or line.startswith("//"):
            continue

        # 2. 判断函数^^函数处理^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    
        #if ff_end and re.search(r"^\w+.*\s\w+\(", line) and line.find(";") == -1:    
        if ff_end and line.find("(") != -1:
            ff_end = 0
            ff1 = 1
            print(index, "ff1")
            if line.find(")") != -1:
                ff2 = 1
                print(index, "ff1 and ff2")
                print(f"\t\t\t 函数是：{line}")
                continue
        
        # “）” 跨行情况
        if ff1 and ff2 == 0:
            if line.find(")") != -1:
                ff2 = 1
                print(index, "ff1 and ff2")
                continue

        if ff1 and ff2:
            if line.startswith("{"):            # 其实只用首行 “{” 就可以判断函数开始; 实际读出的不在首行到了首行
                ff3 = 1
                print(index, "func_start! add debug here^^^^^^^^")
                # 行号打印到文本显示行号， 用来显示
                #out_text += f'\tmy_debgu("shl add");   ------ source index = {index + 1}\n'

                # 正式写入代码
                # out_text += f'\tmy_dbg(" [{index}]  shl_add\\n");\n'
                out_text += f'\tf_start_hook({index});\n'
        
        if ff1 and ff2 and ff3:
            if line.startswith("}"):
                print("func end =======================")

                ff1 = 0
                ff2 = 0
                ff3 = 0
                ff_end = 1

                out_text += f'\tf_end_hook();\n'
                out_text += line + '\n'

    print("=================行处理结束=============================")
    return out_text




def process_c_file(c_file_path):
    print("\t\t c file_path = ", c_file_path)

    fin = open(c_file_path, 'r', encoding="utf-8", newline='\n')
    text = fin.read()
    fin.close()

    text = process_text(text)

    #with open(c_file_path, 'w', encoding='utf-8') as file:
    #    file.truncate(0)

    fin = open(c_file_path, 'w', encoding="utf-8", newline='\n')
    fin.write(text)
    fin.close()


def os_walk_add_dmesg(dir):
    for dirpath, dirnames, filenames in os.walk(dir):
        # a. 打印当前目录路径
        print(f'正在遍历路径: {dirpath}')

        if dirpath in skip_dirs:
            print("skip dirpath:", dirpath)
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

                if filename.endswith(".c"):
                    file_path = os.path.join(dirpath, filename)
                    process_c_file(file_path)   # 开始处理文本 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        print("\n")




if __name__ == '__main__':
    skip_dirs = ['00_c_code\simple\dir_b', 'dir_a']


    if len(sys.argv) >= 2:
        dir = sys.argv[1]
    else:
        dir = '.\\'


    if sys.argv[1].endswith(".c"):
        print(f"single file: {sys.argv[1]}")
        process_c_file(sys.argv[1])
    
    else:
        os_walk_add_dmesg(sys.argv[1])