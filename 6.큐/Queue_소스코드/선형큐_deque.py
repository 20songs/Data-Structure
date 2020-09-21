#deque이용

import collections
q = collections.deque()   # 덱 생성

q.append(1)   #enQueue
q.append(2)   #enQueue
q.append(3)   #enQueue

print(q.popleft()) #deQueue
print(q.popleft()) #deQueue
print(q.popleft()) #deQueue
