def applyToEach(L,f):
    for i in range(len(L)):
        L[i] = f(L[i])
L = [1,-2,3.66]
print('L = ',L)
print('Apply abs to each element of L.')
applyToEach(L,abs)
print('L = ',L)
print('Apply it to each element of L.')
applyToEach(L,int)
print('L = ',L)



def factR(n):
    if n==1:
        return n
    else:
        return n*factR(n-1)
applyToEach(L,factR)
print('L = ',L)
