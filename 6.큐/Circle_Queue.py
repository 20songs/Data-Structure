# front, rear 이용
SIZE = 4
Q = [0] * SIZE #사이즈
front, rear = 0, 0 #초기값

def isFull():
    if (rear+1) % SIZE == front:
        return 0
    else:
        return 1

def enQueue(item):
    global rear
    if isFull():
        rear = (rear+1) % SIZE #rear += 1
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
        front = (front+1) % SIZE #front +=1
        return Q[front]
    else:
        return 'Queue Empty'

def Qpeek():
    if isEmpty():
        return Q[(front+1)%SIZE]
    else:
        return 'Queue Empty'


enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(Q)
print(deQueue())
enQueue(4)
print(Q)
enQueue(5)
print(Q)