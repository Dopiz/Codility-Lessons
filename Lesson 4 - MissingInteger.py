def solution(A: list):
    A = set(A)
    for idx in range(1, len(A) + 1):
        if idx not in A:
            return idx
    return idx + 1


A = [1, 3, 6, 4, 1, 2]
assert solution(A) == 5

A = [-1, 1, 2, 3]
assert solution(A) == 4

A = [-3, -1]
assert solution(A) == 1

A = [-1, 2, 3]
assert solution(A) == 1
