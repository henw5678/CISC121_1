
def CycleRotation (A, K):
    for k in range(K):
        A.append(A.pop(0))
    return A

def OddOccurrencesInArray(A):
    A.sort()
    for i in range(0, len(A) - 1, 2) :
        if A[i] != A[i+1]:
             return A[i]

def ForgJmp (X, Y, D):
    num = 0
    while (X <= Y):
        X+=D
        num+=1
    return num

def PermMissingElems(A):
    A.sort()
    for i in range(len(A)):
        if A[i] != i+1:
            return i+1

def PermCheck(A):
    A.sort()
    for i in range(len(A)):
        if A[i] != i+1:
            return False
    return True
