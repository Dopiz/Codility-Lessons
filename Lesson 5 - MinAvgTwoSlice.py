# 最小值一定是 2 或 3 個 element 的 Slice

def solution(A: list):
    min_tmp = float('inf')
    length = len(A)
    result = 0
    for idx in range(length - 1):
        slice_2 = sum(A[idx:idx+2]) / 2
        if slice_2 < min_tmp:
            min_tmp = slice_2
            result = idx
        if idx < length - 2:
            slice_3 = sum(A[idx:idx+3]) / 3
            if slice_3 < min_tmp:
                min_tmp = slice_3
                result = idx
    return result


A = [99998, 99998, 99998, 99998]
assert solution(A) == 0

A = [4, 2, 2, 5, 1, 5, 8]
assert solution(A) == 1
