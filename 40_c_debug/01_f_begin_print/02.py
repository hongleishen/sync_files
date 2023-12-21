
#  寻找函数
#  添加 debug

if __name__ == '__main__':

    in_path = "00_c_code/usb.c"
    fin = open(in_path, encoding="utf-8")
    input_file = fin.read()
    #print(input_file)

    in_lines = input_file.split("\n")

    # 全局变量
    text = ""

    """
    s: start
    f: find
    f: function

    1: (
    2: )
    3: {

    f_end : }
    """
    
    ff1 = 0         # find func (
    ff2 = 0         # find func )
    ff3 = 0         # fidn func {
    ff_end = 1      # find func }

    '''
    for index, element in enumerate(in_lines):
        print(f"index = {index}: {element}")
    '''

    for index, line in enumerate(in_lines, start=1):
        text += line + '\n'
        print("\n", index, "--------", line)
        
        if ff_end and line.find("(") != -1:
            ff_end = 0
            ff1 = 1
            print(index, "ff1")
            if line.find(")") != -1:
                ff2 = 1
                print(index, "ff1 and ff2")
                continue
        
        # ) 在第二行情况
        if ff1 and ff2 == 0:
            if line.find(")") != -1:
                ff2 = 1
                print(index, "ff1 and ff2")
                continue

        if ff1 and ff2:
            if line.startswith("{"):
                ff3 = 1
                print(index, "func_start! add debug here^^^^^^^^")
                text += '\n\t' + 'my_debug("shl")' + '\n'
        
        if ff1 and ff2 and ff3:
            if line.startswith("}"):
                print("func end =======================")

                ff1 = 0
                ff2 = 0
                ff3 = 0
                ff_end = 1

    print("=================行处理结束=============================")
    print(text)