def solution(X: int, A: list):
    location = set()
    for idx in range(len(A)):
        location.add(A[idx])
        if len(location) == X:
            return idx
    return -1


A = [1, 3, 1, 4, 2, 3, 5, 4]
X = 5
assert solution(X, A) == 6

A = [1, 5, 2, 1, 4, 3]
X = 6
assert solution(X, A) == -1

A = [1, 5, 1, 4, 3]
X = 5
assert solution(X, A) == -1
