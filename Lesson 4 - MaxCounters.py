def solution(N: int, A: list):
    max_val, tmp_max = 0, 0
    result = [0] * N
    for item in A:
        if item > N:
            max_val = tmp_max
        else:
            if result[item - 1] < max_val:
                result[item - 1] = max_val + 1
            else:
                result[item - 1] += 1
            tmp_max = max(tmp_max, result[item - 1])
    for idx in range(len(result)):
        if result[idx] < max_val:
            result[idx] = max_val
    return result


A = [3, 4, 4, 6, 1, 4, 4]
N = 5
assert solution(N, A) == [3, 2, 2, 4, 2]
