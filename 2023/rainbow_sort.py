def main() -> str:
    N = int(input())
    S = input().split(" ")
    res = []
    seen = set()
    for i, color in enumerate(S):
        if color in seen:
            if color != S[i-1]:
                return "IMPOSSIBLE"
        else:
            seen.add(color)
            res.append(color)
    return " ".join(res)


if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        print(f'Case #{case}: {main()}')
