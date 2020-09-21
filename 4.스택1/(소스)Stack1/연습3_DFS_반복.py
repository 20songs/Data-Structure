'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v):
    s = []
    s.append(v)         # push

    while len(s) != 0:
        v = s.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=" ")
            for w in range(V, 0, -1):  # 반대방향으로 돌림.
                if G[v][w] == 1 and visited[w] == 0:
                    s.append(w)

# import sys
# sys.stdin = open("연습3_input.txt")
V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[0] * (V+1) for j in range(V+1)] #2차원 초기화
visited = [0] * (V+1)

for i in range(E):  #입력
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

for i in range(V+1):  #입력확인
    print("{} {}".format(i, G[i]))

dfs(1)
dfs2(1)
