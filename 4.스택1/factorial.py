

def fact(n): # f(n) = n * f(-1)
    if n == 1:  # basic
        return 1
    else:      # inductive(유도)
        return n * fact(n-1)

print(fact(4))