def solution(A):
    total = sum(A)
    result = float('inf')
    for idx in range(len(A) - 1):
        total -= 2 * A[idx]
        result = min(result, abs(total))
    return result


A = [3, 1, 2, 4, 3]
assert solution(A) == 1

A = [-1001, 1, 999]
assert solution(A) == 1999

A = [0, 0]
assert solution(A) == 0
