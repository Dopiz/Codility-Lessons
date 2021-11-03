# https://app.codility.com/demo/results/training99K92Z-BKG/
def solution(X, Y, D):
    return int((Y - X) / D) + ((Y - X) % D > 0)


X = 10
Y = 85
D = 30
assert solution(X, Y, D) == 3, solution(X, Y, D)


X = 0
Y = 0
D = 5
assert solution(X, Y, D) == 0, solution(X, Y, D)


X = 666666
Y = 1000000000
D = 3333
assert solution(X, Y, D) == 299830, solution(X, Y, D)
