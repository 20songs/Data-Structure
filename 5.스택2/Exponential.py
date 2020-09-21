def Power(Base,Exponent):
    if Exponent == 0 or Base == 0:
        return 1
    if Exponent % 2 == 0:
        NewBase = Power(Base,Exponent//2)
        return NewBase * NewBase
    else:
        print(Exponent)
        NewBase = Power(Base,(Exponent-1)//2)
        return (NewBase * NewBase) * Base

print(Power(2,3))