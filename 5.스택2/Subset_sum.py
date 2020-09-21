Arr = [1,2,3]
N = len(Arr)
A = [0] * N # 1,0
count = 0

def powerset(n,k,cursum):
    if cursum > 10: return
    if n == k:
        print(A, end=" : ")
        for i in range(n):
            if A[i]==1:
                print(Arr[i],end=" ")
        print()
    else:
        #k번째 선택
        A[k] = 1
        powerset(n,k+1,cursum + Arr[k])
        #k번째 비선택
        A[k] = 0
        powerset(n,k+1, cursum)

powerset(N,0)