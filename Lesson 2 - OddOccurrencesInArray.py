def solution(A: list):
    result = 0
    for item in A:
        result ^= item
    return result


A = [9, 3, 9, 3, 9, 7, 9]
assert solution(A) == 7


def solution_2(A: list):
    A = sorted(A)
    result = A[0]
    for idx in range(1, len(A), 2):
        result = result - A[idx] + A[idx+1]
    return result


assert solution_2(A) == 7, solution_2(A)
