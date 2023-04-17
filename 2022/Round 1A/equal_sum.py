import sys
import numpy as np

def custom_output(line):
    print(line)
    sys.stdout.flush()

def process():
    N = int(input())
    
    start = [i for i in range(1, N+1)]

    custom_output(" ".join(map(str, start)))
    
    second = list(map(int, input().split(" ")))
    
    arr = start + second
    #
    sum_array = sum(arr)
    n = 2 * len(start)
    k = sum_array // 2
    dp = np.zeros((n + 1, k + 1))

    for i in range(1, k + 1) :
        dp[0][i] = False
    for i in range(n + 1) :
        dp[i][0] = True
    for i in range(1, n + 1) :
        for currSum in range(1, k + 1) :
            dp[i][currSum] = dp[i - 1][currSum]
            if (arr[i - 1] <= currSum) :
                dp[i][currSum] = (dp[i][currSum] or
                                  dp[i - 1][currSum - arr[i - 1]])
 
    set1, set2 = [], []

    i = n
    currSum = k
 
    while (i > 0 and currSum >= 0) :
        if (dp[i - 1][currSum]) :
            i -= 1
            set2.append(arr[i])
        elif (dp[i - 1][currSum - arr[i - 1]]) :
            i -= 1
            currSum -= arr[i]
            set1.append(arr[i])
    #
    answer = set1
    custom_output(" ".join(map(str, answer)))


if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        process()
