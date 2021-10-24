def solution(A: list, K: int):
    if not A:
        return A
    moving = len(A) - K % len(A)
    return A[moving:] + A[:moving]


A = [3, 8, 9, 7, 6]
K = 3
assert solution(A, K) == [9, 7, 6, 3, 8]

A = [1, 2, 3, 4]
K = 4
assert solution(A, K) == [1, 2, 3, 4]

A = []
K = 0
assert solution(A, K) == []
