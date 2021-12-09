# https://app.codility.com/demo/results/trainingSKKRT8-C6D/

def solution(S: str):
    brackets = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = list()
    for s in S:
        if s in brackets.values():
            stack.append(s)
        elif s in brackets.keys() and stack:
            top = stack.pop()
            if top != brackets[s]:
                return 0
        else:
            return 0
    return 0 if stack else 1


S = "{[()()]}"
assert solution(S) == 1, S

S = "([)()]"
assert solution(S) == 0, S

S = ")("
assert solution(S) == 0, S

S = ")()"
assert solution(S) == 0, S

S = "()"
assert solution(S) == 1, S

S = "([)]"
assert solution(S) == 0, S

S = "(((("
assert solution(S) == 0, S
