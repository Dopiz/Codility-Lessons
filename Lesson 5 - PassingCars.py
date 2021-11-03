def solution(A: list):
    zero_count = 0
    result = 0
    for item in A:
        if item == 0:
            zero_count += 1
        else:
            result += zero_count
    return result if result <= 1000000000 else -1


A = [0, 1, 0, 1, 1]
assert solution(A) == 5


A = [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0]
assert solution(A) == 20, solution(A)
