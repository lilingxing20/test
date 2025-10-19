# """
# re 模块是 Python 中用来处理正则表达式的模块，提供了一系列函数，用于匹配、搜索、替换字符串中的模式
#  1. 匹配模式：re.match()、re.search()
#  2. 搜索模式：re.findall()、re.finditer()
#  3. 替换模式：re.sub()
#  4. 编译模式：re.compile()
#  5. 标志位：re.I、re.M、re.S 等
#  6. 特殊字符：.、*、+、?、{m,n}、[]、() 等
#  7. 转义字符：\d、\D、\w、\W、\s、\S 等
#  8. 分组：()、(?:)、(?P<name>) 等
#  9. 非捕获分组：(?:pattern)
#  10. 命名分组：(?P<name>pattern)
#  11. 反向引用：\g<name>、\g<number> 等
#  12. 断言：(?=pattern)、(?!pattern)、(?<=pattern)、(?<!pattern) 等
#  13. 非捕获断言：(?:pattern)
#  14. 零宽度断言：^、$、\b、\B 等
#  15. split() 方法：根据正则表达式分割字符串
# """

import re


# 1. 匹配模式：re.match()、re.search()
r1 = re.match(r'\d?[A-Z]{3}', '1ASD')
print(f"1. 匹配成功：{r1}")
r1 = re.match(r'\d?[A-Z]{3}', 'AD')
print(f"1. 匹配失败：{r1}")

# 2. 搜索模式：re.findall()、re.finditer()
r2 = re.findall(r'\d?[A-Z]{3}', '1ASD234BCD')
print(f"2. 找到的所有匹配项：{r2}")

# 3. 替换模式：re.sub()
ss = "1ASD234BCD"
r3 = re.sub(r'\d?[A-Z]{3}', 'XX', ss)
print(f"3. 原字符串：{ss} , 替换后的字符串：{r3}")

# 4. 编译模式：re.compile()
r4 = re.compile(r'\d?[A-Z]{3}')
r4_1 = r4.match('1ASD')
print(f"4. 匹配成功：{r4_1}")
r4_2 = r4.match('AD')
print(f"4. 匹配失败：{r4_2}")

# 5. 标志位：re.I、re.M、re.S 等
r5 = re.compile(r'\d?[A-Z]{3}', re.I)
r5_1 = r5.match('1asd')
print(f"5. 匹配成功：{r5_1}")
r5_2 = r5.match('ad')
print(f"5. 匹配失败：{r5_2}")

# 6. 特殊字符：.、*、+、?、{m,n}、[]、() 等
r6 = re.compile(r'\d?[A-Z]{3}')
r6_1 = r6.match('1ASD')
print(f"6. 匹配成功：{r6_1}")
r6_2 = r6.match('AD')
print(f"6. 匹配失败：{r6_2}")

# 7. 转义字符：\d、\D、\w、\W、\s、\S 等
r7 = re.compile(r'\d?[A-Z]{3}')
r7_1 = r7.match('1ASD')
print(f"7. 匹配成功：{r7_1}")
r7_2 = r7.match('AD')
print(f"7. 匹配失败：{r7_2}")

# 8. 分组：()、(?:)、(?P<name>) 等
r8 = re.compile(r'(\d?[A-Z]{3})')
r8_1 = r8.match('1ASD')
print(f"8. 匹配成功：{r8_1}")
r8_2 = r8.match('AD')
print(f"8. 匹配失败：{r8_2}")

# 9. 非捕获分组：(?:pattern)
r9 = re.compile(r'(?:\d?[A-Z]{3})')
r9_1 = r9.match('1ASD')
print(f"9. 匹配成功：{r9_1}")
r9_2 = r9.match('AD')
print(f"9. 匹配失败：{r9_2}")

# 10. 命名分组：(?P<name>pattern)
r10 = re.compile(r'(?P<name>\d?[A-Z]{3})')
r10_1 = r10.match('1ASD')
print(f"10. 匹配成功：{r10_1}")
r10_2 = r10.match('AD')
print(f"10. 匹配失败：{r10_2}")

# 11. 反向引用：\g<name>、\g<number> 等
r11 = re.compile(r'(\d?[A-Z]{3})\1')
r11_1 = r11.match('1ASD1ASD')
print(f"11. 匹配成功：{r11_1}")
r11_2 = r11.match('AD')
print(f"11. 匹配失败：{r11_2}")

# 12. 断言：(?=pattern)、(?!pattern)、(?<=pattern)、(?<!pattern) 等
r12 = re.compile(r'\d?[A-Z]{3}(?=\d)')
r12_1 = r12.match('1ASD2')
print(f"12. 匹配成功：{r12_1}")
r12_2 = r12.match('AD2')
print(f"12. 匹配失败：{r12_2}")

# 13. 非捕获断言：(?:pattern)
r13 = re.compile(r'\d?[A-Z]{3}(?:\d)')
r13_1 = r13.match('1ASD2')
print(f"13. 匹配成功：{r13_1}")
r13_2 = r13.match('AD2')
print(f"13. 匹配失败：{r13_2}")

# 14. 零宽度断言：^、$、\b、\B 等
r14 = re.compile(r'\d?[A-Z]{3}(?=\d)')
r14_1 = r14.match('1ASD2')
print(f"14. 匹配成功：{r14_1}")
r14_2 = r14.match('AD2')
print(f"14. 匹配失败：{r14_2}")

#  15. split() 方法：根据正则表达式分割字符串
r15_1 = re.compile(r'\s+')
r15_1 = r15_1.split('王林   王麻子 小林子,WangLin')
print(f"15. 分割后的字符串：{r15_1}")
r15_2 = re.compile(r'[\s,]+')
r15_2 = r15_2.split('王林   王麻子 小林子,WangLin')
print(f"15. 分割后的字符串：{r15_2}")

# 16. 分组捕获
r0 = re.match(r'^(\w{1,10})-(\d{11})$', 'test-19999999999')
print(f"16. 分组匹配成功：{r0}")
print(f"16. 分组捕获：{r0.groups()}")
# group(0) 和整个表达式想匹配
print(r0.group(0), r0.group(1), r0.group(2))

# 17. 贪婪匹配
# \d+默认是贪婪匹配；将后面的9全部匹配了
r0 = re.match(r'^(test-\d+)(9*)$', 'test-19999999999')
print(f"17. 贪婪匹配成功：{r0}")
print(f"17. 分组捕获：{r0.groups()}")

# 18. 非贪婪匹配
# \d+?变成了非贪婪匹配
r0 = re.match(r'^(test-\d+?)(9*)$', 'test-19999999999')
print(f"18. 非贪婪匹配成功：{r0}")
print(f"18. 分组捕获：{r0.groups()}")

# 19. 预编译正则表达式
# re 模块首先编译正则表达式，再用编译后的模式匹配字符串。
# 如果正则表达式重复使用很多次，可以预编译它，避免每次都编译，提高效率。
c0 = re.compile(r'^(\d{3})-(\d{3,8})$')
r0 = c0.match("100-222")
print(f"19. 预编译匹配成功：{r0}")
print(f"19. 分组捕获：{r0.groups()}")
