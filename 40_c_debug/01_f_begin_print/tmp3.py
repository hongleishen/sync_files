line = "        r1eturn 123"

n = line.find("return")
if n == -1:
    print("not find return")
else:
    print(f"find return at {n}")
    

parts = line.split("return")

print("分割前的部分:", parts[0])
if len(parts) > 1:
    print("分割后的部分:", parts[1])
else:
    print("字符串中没有 'return'")

line = parts[0] + '{f_end_hook();  ' + 'return' + parts[1] + '}'
print(line)