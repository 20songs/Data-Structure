
# 문자열 뒤집기

def str_rev(str):
    # str -> list
    arr = list(str)
    # swap
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    # join
    str = "".join(arr)
    return str

#--------------
ss = "algorithm"
print(ss)
sr = str_rev(ss)
print(sr)

## 슬라이싱싱 연산
print(ss[::-1])

##------------
str2 = "algorithm"
arr2 = list(str2)
arr2.reverse()
str2="".join(arr2)
print(str2)


# 문자열 뒤집기 수공예

strings = "algorithm"
arr = list(strings)

for i in range(len(arr)//2):
    arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]

rev = "".join(arr)
print(rev)

print(strings[::-1])