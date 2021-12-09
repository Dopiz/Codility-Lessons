# https://app.codility.com/demo/results/trainingSTXAPA-C7G/

def solution(H: list):
    stack = list()
    stone = 0
    for idx in range(len(H)):
        while stack and stack[-1] > H[idx]:
            stack.pop()
        if not stack or stack[-1] < H[idx]:
            stack.append(H[idx])
            stone += 1
    return stone


H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
assert solution(H) == 7

H = [1]
assert solution(H) == 1

H = [5, 7, 9, 6, 7]
assert solution(H) == 5
