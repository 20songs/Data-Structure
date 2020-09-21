
def dfs2(v):
    stack = []
    stack.append(v)
    while len(stack):
        v = stack.pop()
        if visited[v] ==0:
            visited[v] = 1
            print(v, end=' ')
            for w in range(1, V + 1):
                if G[v][w] == 1 and visited[w] == 0:
                    stack.append(w)


# 정점, 간선
# V,W = map(int,input().split())
V, W = 7,8

# 간선 집합
# numbers = list(map(int,input().split()))
numbers = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

# 인접 행렬
G = [[0]* (V+1) for _ in range(V+1)]

# 방문 체크
visited = [0] * (V+1)

# 간선을 인접 행렬에 입력, 저장
for i in range(W):
    r, c = numbers[2*i], numbers[2*i +1]
    G[r][c] = 1
    G[c][r] = 1

# for i in range(V+1):
#     print("{} {}".format(i,G[i]))

print(dfs2(1))