def solution(A):
    return int((1 + len(A) + 1) * (len(A) + 1) / 2) - sum(A)


A = [2, 3, 1, 5]
assert solution(A) == 4, solution(A)

A = [1]
assert solution(A) == 2, solution(A)
