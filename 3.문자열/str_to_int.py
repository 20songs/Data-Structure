
str1 = "123"
str2 = "12.3"

print(int(str1),type(int(str1))) # 123
print(float(str2),type(float(str2))) # 12.3

str3 = "1+2"
print(str3)            
print(repr(str3))
print(eval(str3))
print(eval(repr(str3)))
print(eval(eval(repr(str3))))

num1 = 123
num2 = 12.3

print(str(num1),type(str(num1)))
print(repr(num1),type(repr(num1)))
print(str(num2),type(str(num2)))
print(repr(num2),type(repr(num2)))