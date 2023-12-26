def count_starting_tabs(line):
    count = 0
    for char in line:
        if char == "\t":
            count += 1
        else:
            break
    return count

# 示例使用
line = "            hello this is str"
#tabs = 0
tabs = count_starting_tabs(line)
print("字符串开头的Tab数量:", tabs)
