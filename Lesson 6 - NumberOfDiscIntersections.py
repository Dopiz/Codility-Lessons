# https://app.codility.com/demo/results/training9KJA7H-VEY/

def solution(A: list):
    range_points = []
    for idx in range(len(A)):
        range_points.append((idx - A[idx], 0))
        range_points.append((idx + A[idx], 1))
    range_points = sorted(range_points)
    count, total = 0, 0
    for item in range_points:
        flag = item[1]
        if flag == 0:
            total += count
            count += 1
        else:
            count -= 1
        if total > 10000000:
            return -1
    return total


A = [1, 5, 2, 1, 4, 0]
res = solution(A)
assert res == 11, res
