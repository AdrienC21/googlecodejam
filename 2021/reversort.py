def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def reversortCost():
    n = int(input())
    L = list(map(int, input().split(" ")))
    if n <= 1:
        return 0
    tot_cost = 0
    for i in range(n-1):
        mind = i
        mv = L[mind]
        for j in range(i+1, n):
            if L[j] < mv:
                mv = L[j]
                mind = j
        reverse(L, i, mind)
        tot_cost += (mind - i + 1)
    return tot_cost

if __name__ == '__main__':
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        print(f'Case #{case}: {reversortCost()}')
