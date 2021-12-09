# https://app.codility.com/demo/results/trainingA4R42U-T7R/

def solution(A: list, B: list):
    survive, stack = len(A), list()
    for idx in range(survive):
        if B[idx] == 1:
            stack.append(A[idx])
        elif stack:
            while stack:
                survive -= 1
                if stack[-1] < A[idx]:
                    stack.pop()
                else:
                    break
    return survive


A = [4, 2, 3, 1, 5]
B = [1, 0, 0, 0, 0]
assert solution(A, B) == 1

A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
assert solution(A, B) == 2

A = [4, 3, 2, 6, 5]
B = [0, 0, 0, 0, 0]
assert solution(A, B) == 5

A = [4, 2, 3, 6, 5]
B = [1, 1, 0, 0, 0]
assert solution(A, B) == 2
