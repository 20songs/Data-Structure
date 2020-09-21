# front, rear 이용
Q = [0] * 100
front, rear = -1, -1

def isFull():
    if rear == len(Q) -1 :
        return 0
    else:
        return 1

def enQueue(item):
    global rear
    if isFull():
        rear += 1
        Q[rear] = item
    else:
        return 'Queue Full'

def isEmpty():
    if front == rear:
        return 0
    else:
        return 1

def deQueue():
    global front
    if isEmpty():
        front += 1
        return Q[front]
    else:
        return 'Queue Empty'

def Qpeek():
    if isEmpty():
        return Q[front+1]
    else:
        return 'Queue Empty'


enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())