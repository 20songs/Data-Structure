arr = [1,2,3]

N = len(arr)

A = []

def powerset(n,k):
    if n == k:
        print(A)
    else:
        A.append(arr[k])
        powerset(n,k+1)
        A.pop()

        powerset(n,k+1)

powerset(N,0)