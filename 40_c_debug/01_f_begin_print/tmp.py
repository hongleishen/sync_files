def split_on_return(s):
    parts = s.split("return")  # 使用1作为第二个参数，确保字符串只被分割一次
    return parts

# 示例
#line = "这是一行字符串，其中包含return关键字"
line = "        return 123"
parts = split_on_return(line)

print("分割前的部分:", parts[0])
if len(parts) > 1:
    print("分割后的部分:", parts[1])
else:
    print("字符串中没有 'return'")


line = parts[0] + '{f_end_hook();  ' + 'return' + parts[1] + '}'
print(line)