from collections import deque

def pancake():
    n = int(input())
    D = list(map(int, input().split(" ")))
    d = deque()
    for elt in D:
        d.append(elt)
    nb = 0
    last = 0
    while d:
        if d[0] <= d[-1]:
            if d[0] >= last:
                nb += 1
                last = d[0]
                d.popleft()
            elif d[-1] >= last:
                nb += 1
                last = d[-1]
                d.pop()
            else:
                # last = max(last, d[0])
                d.popleft()
        else:
            if d[-1] >= last:
                nb += 1
                last = d[-1]
                d.pop()
            elif d[0] >= last:
                nb += 1
                last = d[0]
                d.popleft()
            else:
                # last = max(last, d[-1])
                d.pop()
    return nb

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        print(f'Case #{case}: {pancake()}')
