def solution(A: list):
    length = len(A)
    A = set(A)
    for idx in range(length):
        if idx + 1 not in A:
            return 0
    return 1


A = [4, 1, 3]
assert solution(A) == 0

A = [4, 1, 3, 2]
assert solution(A) == 1

A = [9, 5, 7, 3, 2, 7, 3, 1, 10, 8]
assert solution(A) == 0, A
