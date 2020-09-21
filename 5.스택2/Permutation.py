
def perm(n,k):
    global cnt
    cnt += 1
    if n == k:
        print(arr)
    else:
        for i in range(k,n):
            print('{}번째 k={},i={}'.format(cnt,k,i))
            arr[k], arr[i] = arr[i], arr[k]
            print(arr)
            perm(n,k+1)
            print('{}번째 k={},i={}'.format(cnt,k,i))
            arr[k], arr[i] = arr[i], arr[k]
            print(arr)

cnt = 0
arr = [1,2,3]
N = len(arr)
perm(N,0)
