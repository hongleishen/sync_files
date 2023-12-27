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

in_lines = ["hello", "world", "/**", "* Caller", "* return 0 on"]

for index, line in enumerate(in_lines, start=1):
    print("line = ", line)

    if line.startswith("hello") or line.startswith("/**") or line.startswith("*") \
            or    line.startswith("*/"):
        print("find commit *")
        continue

    print(line,  "       not continue ==================")

