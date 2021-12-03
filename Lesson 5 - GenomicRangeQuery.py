def solution(S: str, P: list, Q: list) -> list:
    N = len(S)  # 字串長度
    M = min(len(P), len(Q))  # Pair 數量
    result = list()
    position = [[-1], [-1], [-1], [-1]]
    genoms = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    for idx in range(1, N + 1):
        for i in range(4):
            position[i].append(position[i][idx - 1])
        position[genoms[S[idx - 1]]][idx] = idx - 1

    for idx in range(M):
        for i in range(4):
            if position[i][Q[idx]+1] >= P[idx]:
                result.append(i + 1)
                break
    return result


S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]
print(solution(S, P, Q))
