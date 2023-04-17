def color(totInk: int) -> str:
    printer1 = list(map(int, input().split(" ")))
    printer2 = list(map(int, input().split(" ")))
    printer3 = list(map(int, input().split(" ")))
    minC = min(printer1[0], min(printer2[0], printer3[0]))
    minM = min(printer1[1], min(printer2[1], printer3[1]))
    minY = min(printer1[2], min(printer2[2], printer3[2]))
    minK = min(printer1[3], min(printer2[3], printer3[3]))
    if minC + minM + minY + minK < totInk:
        return "IMPOSSIBLE"
    if minC > totInk:
        return "{} {} {} {}".format(totInk, 0, 0, 0)
    inkRemaining = totInk - minC
    if minM > inkRemaining:
        return "{} {} {} {}".format(minC, inkRemaining, 0, 0)
    inkRemaining = inkRemaining - minM
    if minY > inkRemaining:
        return "{} {} {} {}".format(minC, minM, inkRemaining, 0)
    inkRemaining = inkRemaining - minY
    return "{} {} {} {}".format(minC, minM, minY, inkRemaining)
    
if __name__ == "__main__":
    test_cases = int(input())
    totInk = 10**6
    for case in range(1, test_cases + 1):
        print(f'Case #{case}: {color(totInk)}')
