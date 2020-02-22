"""输出一个字符串中次数最多的字母和次数"""
s="aaaaaaaaaaaabbcccccddxxxxffff"
max_s_count = 0
max_s_count_letters = []
for i in s:
    if s.count(i) > max_s_count:
        max_s_count_letters = []
        max_s_count = s.count(i)

    if s.count(i) == max_s_count:
        max_s_count_letters.append(i)
        max_s_count = s.count(i)
print(list(set(max_s_count_letters)), max_s_count)

