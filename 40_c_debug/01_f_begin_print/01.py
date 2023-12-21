import re

# 函数匹配的正则表达式
function_pattern = re.compile(r'\w+\s+\w+\s*\([^)]*\)\s*\{')

# 打开并读取文件
def find_functions_in_c_file(file_path):
    print("====")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for l in lines:
        print(l)

    # 遍历每一行，查找函数
    for line_number, line in enumerate(lines, start=1):
        print(line_number, line)
        if function_pattern.search(line):
            # 提取函数名
            function_name = re.search(r'\w+\s+(\w+)\s*\(', line).group(1)
            print(f"行号: {line_number}, 函数名: {function_name}")

if __name__ == "__main__":
    file_path = "./00_c_code/usb.c"
    find_functions_in_c_file(file_path)


    '''
    with open(file_path, 'r') as file:
        for line in file:
            print(line)  # 使用strip()方法去除行尾的换行符
    '''