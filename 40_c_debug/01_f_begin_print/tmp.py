import os

# 指定要遍历的文件夹路径
folder_path = '您的文件夹路径'

# 不需要处理的子目录名列表
skip_dirs = ['不需要处理的子目录1', '不需要处理的子目录2']

# 遍历文件夹及其子目录中的每个文件
for root, dirs, files in os.walk(folder_path):
    # 过滤掉不需要处理的子目录
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    
    for filename in files:
        if filename.endswith('.c'):  # 仅处理以 .c 结尾的文件
            file_path = os.path.join(root, filename)
            
            # 读取文件
            with open(file_path, 'r') as file:
                text = file.read()

            # 在文本中进行修改
            # 假设您将 "old_text" 替换为 "new_text"
            text = text.replace('old_text', 'new_text')

            # 将修改后的文本写回文件
            with open(file_path, 'w') as file:
                file.write(text)