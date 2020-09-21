# arr: <class 'list>: [[1,2,3],[4,5,6],[7,8,9]]
arr = [ [1,2,3],
        [4,5,6],
        [7,8,9]]

N = len(arr)    # 행의 길이
M = len(arr[0]) # 열의 길이

# 행 우선 검색
for i in range(N):
    for j in range(M):
        print(arr[i][j],end=" ")
    print()
print()

# 열 우선 검색

for j in range(M):
    for i in range(N):
        print(arr[i][j],end= " ")
    print()
print()