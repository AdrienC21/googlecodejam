def draw():
    R, C = list(map(int, input().split(" ")))
    print(".." + (C-1) * "+-" + "+")
    print(".." + (C-1) * "|." + "|")
    R -= 1
    for _ in range(R):
        print(C * "+-" + "+")
        print(C * "|." + "|")
    print(C * "+-" + "+")

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        print(f'Case #{case}:')
        draw()
