def maxStraight():
    n = int(input())
    S = list(map(int, input().split(" ")))
    S.sort()
    i = 0
    maxS = 0  # maxStraight
    intToTest = 1
    maxDice = S[-1]
    while i < n:
        if S[i] >= intToTest:
            maxS += 1
            intToTest += 1

        # we will not find a dice large enough from now on
        if intToTest > maxDice:
            break
        i += 1
    return maxS

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        print(f'Case #{case}: {maxStraight()}')
