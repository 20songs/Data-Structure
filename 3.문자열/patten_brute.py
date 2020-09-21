
def brute(t,p):
    i,j = 0,0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(p):
        return i - len(p)
    else:
        return -1

def brute2(text,pattern):
    for i in range(len(text)-len(pattern)+1):
        cnt=0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else: cnt += 1
        if (cnt >= len(pattern)): return i
    return -1


test = "a pattern matching algorithm part 1"
pattern = "rithm"

N = len(test)
M = len(pattern)

i = 0
j = 0

while i < N and j < M:
    if test[i] != pattern[j]:
        i = i-j
        j = -1
    i += 1
    j += 1
if j == M:
    print(test[i-M:i])
else:
    print(-1)
