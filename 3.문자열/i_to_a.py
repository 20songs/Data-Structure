
def itoa(num):
    x = num # 몫
    y = 0 # 나머지
    arr = []
    while x:
        y = x % 10
        x = x // 10
        arr.append(chr(y+ord('0')))
        # 아스키 코드 출발점을 지정해주려고 ord(0)사용
    arr.reverse()
    strings = "".join(arr)
    return strings


x = 123
print(x,type(x))

str1 = itoa(x)
print(str1, type(str1))