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