
str1 = "abc 1,2 ABC"
print(str1)

str1 = str1.replace("1,2","one,two")
print(str1)

# 본래는 문자열 - 리스트 변환
# 1,2 뒷 부분을 보관하고
# one, two를 변경한 후
# 보관한 값을 덧붙인 다음
# 리스트 -> 문자열 재변환 