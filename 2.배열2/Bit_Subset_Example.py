
arr =[-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
cnt = 0
for i in range(1,1<<n): # 0, 공집합은 제외
    sum = 0
    for j in range(n):
        if i & (1<<j):
            sum += arr[j]
    if sum==0:
        cnt+=1

print(cnt,1<<n) #42