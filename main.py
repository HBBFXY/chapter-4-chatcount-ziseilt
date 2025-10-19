# 从键盘输入一行字符
text = input()

# 初始化计数器
letters = 0
digits = 0
spaces = 0
others = 0

# 遍历每个字符并分类统计
for char in text:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':  # 只统计英文字母
        letters += 1
    elif '0' <= char <= '9':  # 判断是否为数字
        digits += 1
    elif char == ' ':  # 判断是否为空格
        spaces += 1
    else:
        others += 1

# 按照要求格式输出结果
print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")
