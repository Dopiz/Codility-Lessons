def solution(A: int, B: int, K: int):
    bottom = int(A / K) + (A % K > 0)
    top = int(B / K)
    return top - bottom + 1


A, B, K = 6, 11, 2
assert solution(A, B, K) == 3

A, B, K = 6, 6, 2
assert solution(A, B, K) == 1

A, B, K = 0, 11, 2
assert solution(A, B, K) == 6
