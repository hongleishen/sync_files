numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number % 2 == 0:  # 检查数字是否为偶数
        print("%2 = 0")
        c =6 + 4
        continue        # 如果是偶数，跳过后续代码，继续下一次循环

    if number % 5 == 0:
        print(f"{number}%4 == 0")
        continue

    print(number)  # 只有当数字不是偶数时，这行代码才会执行
