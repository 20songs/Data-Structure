
def fibo2(n):
    if n>= 2 and len(memo) <= n:
        memo.append(fibo2(n-1)+fibo2(n-2))
    return memo[n]


memo = [0,1]    #참조형(RW)
ans = 0         #값형(R)
print(fibo2(998))