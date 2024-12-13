def fibRecursive(i):
    F = [0] * (i+1)
    def fib(i):
        if i < 2:
            return i 
        if F[i] != 0:
            return F[i]
        F[i] = fib(i-1) + fib(i-2)
        return F[i]
    
    return fib(i)

def fibIterative(i):
    F = [0, 1]
    for j in range(2, i+1):
        F.append(F[j-1] + F[j-2])
        
    return F[i]

def fibIterativeConstantSpace(i):
    a, b = 0, 1
    for _ in range(2, i+1):
        a, b = b, a + b
    
    return b

a = 1000000

print(fibIterativeConstantSpace(a))