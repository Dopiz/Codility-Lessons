# https://app.codility.com/demo/results/trainingSKKRT8-C6D/

def solution(S: str):
    stack = list()
    for s in S:
        if s == "(":
            stack.append(s)
        elif s == ")" and stack:
            top = stack.pop()
            if top != "(":
                return 0
        else:
            return 0
    return 0 if stack else 1


S = ")("
assert solution(S) == 0, S

S = ")()"
assert solution(S) == 0, S

S = "())"
assert solution(S) == 0, S

S = "(((("
assert solution(S) == 0, S

S = "(()(())())"
assert solution(S) == 1, S
