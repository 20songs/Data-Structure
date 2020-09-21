
def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(': #push
            stack.append(i)
        elif arr[i] == ')': #pop 비교
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True

stack = []
arr = "()()((()))"
arr2 = "()()((())))"

print(check(arr))
print(check(arr2))