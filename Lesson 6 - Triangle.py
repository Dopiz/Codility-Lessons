# https://app.codility.com/demo/results/trainingDMG2TN-ZK9/

def solution(A: list):
    A = sorted(A)
    for idx in range(len(A) - 2):
        p, q, r = A[idx], A[idx + 1], A[idx + 2]
        if p + q > r and p + r > q and r + q > p:
            return 1
    return 0


A = [10, 2, 5, 1, 8, 20]
assert solution(A) == 1

A = [10, 50, 5, 1]
assert solution(A) == 0
