'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(G, v):                      # 그래프G, 탐색시작점 v
    visited = [0] * (V+1)           # V : 정점수
    queue=[]                        # 큐 생성

    queue.append(v)                 # 시작점 v를 enQueue
    visited[v] = 1                  # 방문한 것으로 표시

    while queue:                    # queue가 비어있지 않으면
        t = queue.pop(0)            # deQueue
        print(t, end=" ")
        for w in G[t]:              # t의 인접한 모든 정점에 대하여
            if not visited[w] :     # 방문하지 않았으면
                queue.append(w)     # 인접정점 w를 enQueue
                visited[w] = 1      # 방문표시

import sys
sys.stdin = open("연습3_input.txt")
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = {i:[] for i in range(1, V+1)}   # 인접리스트

for i in range(E):  #입력
    s,e = temp[2*i], temp[2*i+1]
    G[s].append(e)
    G[e].append(s)

print(G)        # 입력 확인
bfs(G, 1)