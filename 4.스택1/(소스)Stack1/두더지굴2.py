
import sys
sys.stdin = open("두더지굴_input.txt")

def dfs(x, y, color):
    visited[x][y] = color

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= N: continue
        if ny < 0 or ny >= N: continue
        if arr[nx][ny] == 0: continue
        if visited[nx][ny] != 0: continue

        dfs(nx, ny, color)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            dfs(i, j, cnt)

count = [0] * (cnt+1)

for i in range(N):
    for j in range(N):
        for k in range(1, len(count)):
            if visited[i][j] == k:
                count[k] += 1

count.sort(reverse=1)
print(cnt)
for i in range(len(count)-1):
    print(count[i])


