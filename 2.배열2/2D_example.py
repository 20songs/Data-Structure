'''
5 5
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''
# input
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# explore nearby

n = len(arr)
m = len(arr[0])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

total = 0
sum_list = []
for x in range(n):
    for y in range(m):
        sum = 0
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            #if newx >= 0 and newx < N and newy >= 0 and newy < M:
            if newx <0 or newx >=5:continue
            if newy <0 or newy >=5:continue

            if arr[x][y] - arr[newx][newy] > 0:
                sum += arr[x][y] - arr[newx][newy]
            else:
                sum += arr[newx][newy] - arr[x][y]
        sum_list.append(sum)
        total += sum
print(total,sum_list)






