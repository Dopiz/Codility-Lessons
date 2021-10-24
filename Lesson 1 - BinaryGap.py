def solution(N: int):
    N = "{0:b}".format(N)
    result = 0
    start = 0
    for idx in range(1, len(N)):
        if N[idx] == "1":
            result = max(result, idx - start - 1)
            start = idx
    return result


N = 32
assert solution(N) == 0
N = 1041
assert solution(N) == 5
