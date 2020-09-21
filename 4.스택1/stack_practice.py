# C style

def push_stack(item):
    global top
    if top > 100 - 1:
        return
    else:
        top += 1
        stack[top] = item

def pop_stack(): # isEMPTY 체크
    global top
    if top == -1:
        result = "Stack is Empty!!!"
        return result
    else:
        result = stack[top]
        top -= 1
        return result

stack = [0] * 100 # 고정 [배열은 고정]
top = -1

push_stack(1)
push_stack(2)
push_stack(3)
print(pop_stack())
print(pop_stack())
print(pop_stack())
print(pop_stack())