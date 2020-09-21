
def atoi(strings):
    value = 0
    for i in range(len(strings)):
        c = strings[i]
        # 0~9
        if c >= '0' and c <= '9': # ASCII 코드로 비교 가능함, 연산자 오버로딩
            digit = ord(c) - ord('0')   #c - ('0'은 안된다XX
        else:
            break
        value = value * 10 + digit
        # value = value*10 + c
        # value = value*10 + ord(c) - ord('0')
    return value

a = "123"
print(type(a))
print(a)
b = atoi(a)
print(type(b))
print(b)