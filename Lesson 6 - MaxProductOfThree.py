# https://app.codility.com/demo/results/trainingZW3KCH-QUA/

def solution(A: list):
    A = sorted(A)
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])


A = [-3, 1, 2, -2, 5, 6]
assert solution(A) == 60
