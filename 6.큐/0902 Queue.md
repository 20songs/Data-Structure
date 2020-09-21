[toc]

# 0902 Queue

## 큐 개요

* 큐
* 우선순위 큐
  * Tree(Heap)
* BFS
  * 넓이 우선 탐색
* 큐의활용: 버퍼



### 큐

---

> front, rear

#### 큐의 특성

* 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료 구조
  * 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조
  * 입구(삽입)와 출구(삭제)가 별개로 존재하는 자료형
* 선입선출구조(FIFO)
  * 큐에 삽입한 순서대로 원소가 저장되어, 
  * 가장 먼저 삽입되는 원소는 가장 먼저 삭제된다.
  * 예: 서비스 대기 행렬

#### 큐의 선입 선출 구조

| 0                  | 1    | 2    | 3    | 4    | 5                 |
| ------------------ | ---- | ---- | ---- | ---- | ----------------- |
| Delete/머리(Front) |      |      |      |      | Insert/꼬리(Rear) |



#### 큐의 주요 연산

| 연산          | 기능                                                |
| ------------- | --------------------------------------------------- |
| enQueue(item) | 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산         |
| deQueue()     | 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산  |
| createQueue() | 공백 상태의 큐를 생성하는 연산                      |
| isEmpty()     | 큐가 공백상태인지 확인하는 연산                     |
| isFull()      | 큐가 포화상태인지 확인하는 연산                     |
| Qpeek()       | 큐의 앞쪽(front)에서 원소를 삭제 없이 반환하는 연산 |



#### 큐의 연산 과정

1) 공백 큐 생성: creqteQueue();

* Q = [0] * 100; front = rear = -1

  | -1          | 0    | 1    | 2    |
  | ----------- | ---- | ---- | ---- |
  | front, rear |      |      |      |


2) 원소 A 삽입: enQueue(A);

* rear += 1; rear = 0; Q[rear] = A;

| -1    | 0       | 1    | 2    |
| ----- | ------- | ---- | ---- |
| front | rear, A |      |      |

3) 원소 B 삽입: enQueue(B);

* rear += 1; rear = 1; Q[rear] = B;

| -1    | 0    | 1      | 2    |
| ----- | ---- | ------ | ---- |
| front | A    | rear,B |      |

4) 원소 반환/삭제: deQueue();

* front += 1; front = 0; Q.dequeue[front];

| -1   | 0     | 1      | 2    |
| ---- | ----- | ------ | ---- |
|      | front | rear,B |      |

5) 원소 C 삽입: enQueue(C);

* rear += 1; rear = 2; Q[rear] = C;

| -1   | 0     | 1    | 2      |
| ---- | ----- | ---- | ------ |
|      | front | B    | rear,C |

6) 원소 반환/삭제: deQueue();

* front += 1; front = 1; Q.dequeue[front];

| -1   | 0    | 1     | 2    |
| ---- | ---- | ----- | ---- |
|      |      | front | C    |

* front의 자리에는 원소가 없다
  * 개념상 front는 최 우선 원소의 앞 부분에 해당함
  * 그러므로 front == rear인 경우 Queue는 비어있는 isEmpy() 상태이다



#### 큐의 구현

* 선형큐
  * 1차원 배열을 이용한 큐
    * 큐의 크기 = 배열의 크기
    * front: 저장된 첫 번째 원소의 인덱스(+1)
    * rear: 저장된 마지막 원소의 인덱스
  * 상태표현
    * 초기 상태: front = rear = -1
    * 공백 상태: front = rear [isEmpty]
    * 포화 상태: rear = n-1 (n:배열의 크기, n-1:배열의 마지막 인덱스)

* 순서

  1) 초기: createQueue()

  * 초기 공백 큐 생성
    * 크기 n인 1차원 리스트
    * front, near = -1 초기화

  2) 삽입: enQueue()

  * 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    * 1) rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
    * 2) 그 인덱스에 해당하는 리스트원소 Q[rear]에 item 저장

  ```python
  def enQueue(item):
      global rear
      if isFull(): print("Queue_Full")
      else:
          rear += 1
          Q[rear] = item
  ```

  3) 삭제: deQueue()

  * 가장 앞에 있는 원소를 삭제하기 위해
    * 1) 프론트 값을 하나 증가시켜 큐에 남아있는 첫 번째 원소로 이동
    * 2) 새로운 첫 번째 원소를 리턴함으로써 삭제와 동일한 기능

  ```python
  def deQueue():
      global front
      if isEmpty(): print("Queue_Empty")
      else:
          front += 1
          return Q[front]
  ```

  4) 공백 상태 및 포화상태 검사: isEmpty(), isFull()

  * 공백상태: front = rear
  * 포화상태: rear = n-1
    * (n:배열의 크기,n -1)

  ```python
  def isEmpty():
      return front == rear
  
  def isFull():
      return rear == len(Q) - 1
  ```

  5) 검색: Qpeek()

  * 가장 앞에 있는 원소를 검색하여 반환
  * 현재 front의 한 자리 뒤(front+1)에 있는 원소, 즉 큐의 첫번째에 있는 원소를 반환

  ```python
  def Qpeek():
      if isEmpty(): print("Queue_empty")
      else:
          return Q[front+1]
  ```

* 전체 코드

```python
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
```

```python
#append, pop 이용
Q = []

Q.append(1)
Q.append(2)
Q.append(3)

# pop 0 는 특별한 경우에 시간이 걸림
print(Q.pop(0))
print(Q.pop(0))
print(Q.pop(0))
```



#### 선형 큐 이용 시의 문제점

* 메모리
  * 리스트 크기 고정 -> 사용할 큐의 크기만큼 미리 확보 -> 메모리 낭비
* 잘못된 포화 상태 인식
  * 1) 삽입, 삭제를 계속할 경우 리스트의 앞부분에 활용할 수 있는 공간이 있음에도, rear = n-1 상태 즉, 포화 상태로 인식
  * 2) 더 이상 삽입을 수행할 수 없음



* 해결 방법
  * 1차원 배열을 사용하되, 논리적으로 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정
  * 파이썬 리스트 특성을 사용하여 메모리 절약
    * 단점: 삽입, 삭제 시 복사, 데이터 이동시키는 연산 수행에 많은 시간 소모
  * 단순 연결 리스트 구현 후 메모리 동적 확보
  * 큐 라이브러리 사용
    * `from collections import deque`



#### 원형 큐의 구조

> 1차원 리스트 사용
>
> > 논리적으로 리스트 처음과 끝이 연결되어 원형 구조로 가정함

* 초기 공백 상태
  
  * front = rear = 0
    * cf_ 선형 구조에서는 -1로 초기값을 할당함
  
* Index 순환
  * front와 rear 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스 0으로 이동해야 함
  * 이를 위해 나머지 연산자 mod를 사용함
    * 배열 크기 6, 인덱스 0~5 , %6

* front 변수
  
  * 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
  
* 삽입 위치 및 삭제 위치

  | 테이블 인덱스 | 삽입 위치             | 삭제 위치           |
  | ------------- | --------------------- | ------------------- |
  | 선형 큐       | rear = rear + 1       | front = front + 1   |
  | 원형 큐       | rear = (rear + 1) % n | front = (front+1)%n |



1) 공백 큐 생성: creqteQueue();

* Q = [0] * 100; front = rear = 0

  | 0           | 1    | 2    | 3    |
  | ----------- | ---- | ---- | ---- |
  | front, rear |      |      |      |

2) 원소 A 삽입: enQueue(A);

* rear += 1; rear = 1; Q[rear] = A;

| 0     | 1       | 2    | 3    |
| ----- | ------- | ---- | ---- |
| front | rear, A |      |      |

3) 원소 B 삽입: enQueue(B);

* rear += 1; rear = 2; Q[rear] = B;

| 0     | 1    | 2      | 3    |
| ----- | ---- | ------ | ---- |
| front | A    | rear,B |      |

4) 원소 반환/삭제: deQueue();

* front += 1; front = 1; Q.dequeue[front];

| 0    | 1     | 2    | 3    |
| ---- | ----- | ---- | ---- |
|      | front | B    |      |

5) 원소 C 삽입: enQueue(C);

* rear += 1; rear = 3; Q[rear] = C;

| 0    | 1     | 2    | 3      |
| ---- | ----- | ---- | ------ |
|      | front | B    | rear,C |

6) 원소 D 삽입: enQueue(D);

* rear+= 1; rear= 4; Q.enQueue[rear%4];

| 0      | 1     | 2    | 3    |
| ------ | ----- | ---- | ---- |
| rear,D | front | B    | C    |

* 순서

1) 초기: createQueue()

* 초기 공백 큐 생성
  * 크기 n인 1차원 리스트
  * front, near = 0 초기화

2) 공백 상태 및 포화상태 검사: isEmpty(), isFull()

* 공백상태: front = rear
* 포화상태: 삽입할 rear 의 다음 위치 == 현재 front
  * (rear + 1) % n == front

```python
def isEmpty():
    return front==rear
def isFull():
    return (rear + 1) % len(cQ) = front
```

2) 삽입: enQueue(item)

* 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
  * 1) rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련
    * rear = (rear+1) % n
  * 2) 그 인덱스에 해당하는 리스트원소 cQ[rear]에 item 저장

```python
def enQueue(item):
    global rear
    if isFull(): print("Queue_Full")
    else:
        rear = (rear +1) & len(cQ)
        Q[rear] = item
```

3) 삭제: deQueue()

* 가장 앞에 있는 원소를 삭제하기 위해
  * 1) front 값을 조정하여 삭제할 자리 준비
  * 2) 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능

```python
def deQueue():
    global front
    if isEmpty(): print("Queue_Empty")
    else:
        front = (front+1) % len(cQ)
        return Q[front]
```

* 원형 큐 코드

```python
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
```



#### 리스트 특성 사용하기

* 리스트 특성
  * 리스트는 크기를 동적으로 변경함
  * 메모리 문제 해결
  * 삽입, 삭제 시 복사, 데이터를 이동시키는 연산에 많은 시간 소모
* 리스트 메서드
  * append: 삽입
  * pop(0): 삭제
* 초기값
  * front: -1
  * rear: len(queue)-1



#### 연결 큐

> list 자료구조에서는 다룰 필요 없음/



### 우선순위 큐

---

* 우선순위 큐의 특성
  * 우선순위를 가진 항목들을 저장하는 큐
  * FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.
    * 우선순위가 같은 경우 FIFO
* 우선순위 큐의 적용 분야
  * 시뮬레이션 시스템
  * 네트워크 트래픽 제어
  * 운영체제의 태스크 스케줄링
* 우선순위 큐 구현
  * 다차원 리스트, 배열 이용
  * 라이브러리 이용
* 우선순위 큐 기본 연산
  * 삽입: enQueue
    * 우선순위를 생각하여 삽입
  * 삭제: deQueue



* 배열을 이용하여 우선순위 큐 구현
  * 배열을 이용하여 자료 저장
  * 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
  * 가장 앞에 최고 우선순위 원소가 위치함
* 문제점
  * 리스트 사용에 따라, 삽입-삭제 연산의 원소 재배치 문제 발생
  * 소요 시간
  * 메모리
* 해결방법
  * 힙 자료구조
  * 라이브러리



#### 큐의 활용: 버퍼(Buffer)

---

* 버퍼
  * 데이터를 한 곳에서 다르 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  * 버퍼링: 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미한다.
* 버퍼의 자료구조
  * 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용된다
  * 순서대로 입력/출력/전달되어야 하므로 FIFO방식의 자료구조인 큐가 활용



* Revisit to 마이쮸
  * Queue를 이용하여 마이쮸 나눠주기 시뮬레이션을 해 보자



### BFS(Breadth First Seacrh)

---

* 그래프
  * 비 선형 구조
  * 표현방법: 인접행렬, 인접리스트
  * 순회: DFS, BFS
* 그래프를 탐색하는 방법에는 크게 두 가지가 있음
  * 깊이 우선 탐색(Depth First Search, DFS)
  * 너비 우선 탐색(Breadth First Search, BFS)
* 너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
* 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비 우선 탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함



#### BFS 알고리즘

* enQ시 방문처리

  ```python
  BFS(G,V): 					# 그래프G, 탐색 시작점 V
      visited = [0]*(n+1)		# n: 정점의 개수
      q = []					# 큐 생성
      
      q.append(v)			# 시작정점 v를 enQueue
      visited[v] = 1		# 방문한 것으로 표시
      
      while len(q)!=0:	# 큐가 비어있지 않은 경우
          t=q.pop(0)		# deQueue(왼쪽 원소 반환)
          for w in G[t]:	#정점 t와 인접한 정점 w에 대해
              if not visited[w]:		#방문하지 않은 곳이라면
                  q.append(w)		# enQue
                  visitedpw[w] = (visited[t] +) 1	#방문 표시
  ```

  * DFS의 알고리즘과 유사함
    * 방문처리 v
    * v의 인접정점(w) and 방문안한 정점 dfs(w)
  * 장점:
    * enQ의 경우 출발점에서 얼마나 떨어져 있는지 visited를 통해 확인할 수 있음
  * deQ 알고리즘
    * visit 처리하는 순서가 다름

  ```
  
  ```

  

#### BFS 예제

* 인접 행렬

```python
def bfs(v):
    # 큐, 방문
    Q = []
    visit = [0] * (V+1)
    #enQ(v), visit(v)
    Q.append(v)
    visit[v] = 1
    print(v,end=" ")
    # 큐가 비어있지 않은 동안
    while Q:
        # v = deQ()
        v = Q.pop(0)
        # v의 인접한 정점(w), 방문 안 한 정점이면
        for w in range(1,V+1):
            if G[v][w] == 1 and visit[w] == 0:
            #enQ(v), visit(v)
                Q.append(w)
                visit[w] = 1
                print(w,end=" ")

#입력
V,E = map(int,input().split())
temp = list(map(int,input().split()))
#인접행렬 초기화
G = [[0]*(V+1) for _ in range(V+1)]
#인접행렬 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i + 1]
    G[s][e] = G[e][s] = 1

for i in range(1,V+1):
    print("{} {}".format(i,G[i]))

bfs(1)
```

* 인접 리스트, 멀리 떨어진 값 구하기

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v):
    # 큐, 방문
    Q = []
    # visit = [0] * (V+1)    #단순 방문일때
    #enQ(v), visit(v)
    Q.append(v)
    visit[v] = 1
    print(v,end=" ")
    # 큐가 비어있지 않은 동안
    while Q:
        # v = deQ()
        v = Q.pop(0)
        # v의 인접한 정점(w), 방문 안 한 정점이면
        for w in G[v]:
            if not visit[w]:
            #enQ(v), visit(v)
                Q.append(w)
                # visit[w] = 1 # 단순 방문 여부 확인일때
                visit[w] = visit[v] + 1
                print(w,end=" ")

#입력
V,E = map(int,input().split())
temp = list(map(int,input().split()))
#인접 리스트 초기화
G = [[]for _ in range(V+1)]
visit = [0] * (V+1)
#인접행렬 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i + 1]
    G[s].append(e)
    G[e].append(s)

for i in range(1,V+1):
    print("{} {}".format(i,G[i]))
print(G)
bfs(1)

# 1번에서 가장 멀리 있는 정점의 번호, 몇 칸 떨어져있는가?
max_idx= 0
for i in range(1,V+1):
    if visit[max_idx] < visit[i]:
        max_idx= i
print(max_idx,visit[max_idx]-1)
```

* 딕셔너리, 값찾기

```python
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v):
    # 큐, 방문
    Q = []
    # visit = [0] * (V+1)    #단순 방문일때
    #enQ(v), visit(v)
    Q.append(v)
    visit[v] = 1
    print(v,end=" ")
    # 큐가 비어있지 않은 동안
    while Q:
        # v = deQ()
        v = Q.pop(0)
        # v의 인접한 정점(w), 방문 안 한 정점이면
        for w in G[v]:
            if not visit[w]:
            #enQ(v), visit(v)
                Q.append(w)
                # visit[w] = 1 # 단순 방문 여부 확인일때
                visit[w] = visit[v] + 1
                print(w,end=" ")

#입력
V,E = map(int,input().split())
temp = list(map(int,input().split()))
#인접 리스트 초기화
G = {i:[]for i in range(V+1)}
visit = [0] * (V+1)
#인접행렬 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i + 1]
    G[s].append(e)
    G[e].append(s)

for i in range(1,V+1):
    print("{} {}".format(i,G[i]))
print(G)
bfs(1)

# 1번에서 가장 멀리 있는 정점의 번호, 몇 칸 떨어져있는가?
max_idx= 0
for i in range(1,V+1):
    if visit[max_idx] < visit[i]:
        max_idx= i
print(max_idx,visit[max_idx]-1)
```

