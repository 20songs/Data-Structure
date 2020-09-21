'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(v):
    visited = [0 for _ in range(V+1)]
    queue=[]

    queue.append(v)
    visited[v] = 1

    while len(queue) != 0:
        t = queue.pop(0)  # deQueue 때 출력
        print(t, end=" ")
        for w in range(1, V+1):
            if G[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = 1

def bfs2(v):
    global G, V
    visited = [0] * (V+1)
    queue=[]

    queue.append(v)

    while len(queue) != 0:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=" ")
            for w in range(V+1):
                if G[v][w] == 1 and visited[w] == 0:
                    queue.append(w)


import sys
sys.stdin = open("연습3_input.txt")
V, E = map(int, input().split())

temp = list(map(int, input().split()))

G = [[0 for i in range(V+1)] for j in range(V+1)] #2차원 초기화

for i in range(E):  #입력
    s,e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

for i in range(V+1):  #입력확인
    print("{} {}".format(i, G[i]))

bfs(1)

