def solution(A):
    A.sort()
    for i in range(len(A)-1):
        if A[i] != i + 1:
            return 0
    return 1
    pass
