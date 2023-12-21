import os

def test_os_walk(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        print(f'当前目录: {foldername}')
        for subfolder in subfolders:
            print(f'子文件夹: {os.path.join(foldername, subfolder)}')
        for filename in filenames:
            print(f'文件: {os.path.join(foldername, filename)}')

if __name__ == "__main__":
    directory_to_walk = "00_c_code\simple"  # 将此路径替换为你要测试的目录路径
    test_os_walk(directory_to_walk)
