stack = []

def push_stack(item):
    stack.append(item)

def pop_stack():
    if len(stack) == 0:
        result = "Stack is empty"
        return result
    else:
        return stack.pop()

push_stack(1)
push_stack(2)
push_stack(3)
print(pop_stack())
print(pop_stack())
print(pop_stack())
print(pop_stack())