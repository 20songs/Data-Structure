
arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]]

N = len(arr)
M = len(arr[0])

#상하 좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 대각선도 가야 한다면
# dx = [0, 0, -1, 1, 1, -1, 1, -1]
# dy = [-1, 1, 0, 0, 1, -1, -1, 1]

# visited
visited =[[0 for _ in range(M)] for _ in range(N)]
#visited = [[0] * m for _ in range(n)]
# visited = [[0]*m]*n #(X)

for x in range(N):
    for y in range(M):
        for i in range(4):
            testx = x + dx[i]
            testy = y + dy[i]
            #인덱스 체크
            #if 0<= testx < N and 0 <= texty < M and visited[testx][testy] == 0: #파이썬 only
            #if testx >= 0 and testx < N and testy >= 0 and testy < M and visited[testx][testy]:
            if testx < 0 or testx >= N : continue
            if testy < 0 or testy >= M : continue
            if visited[testx][testy]==1 : continue
            print(arr[testx][testy],end= " ")
            #재방문 체크
            visited[testx][testy] = 1

        print()
