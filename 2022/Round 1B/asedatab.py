import numpy as np
import sys

def custom_output(line):
    print(line)
    sys.stdout.flush()

def process():
    Ni = -1

    s = "11111111"
    # print(s, flush=True)
    custom_output(s)
    Ni = int(input())
    nb_ones = 8 - Ni

    tried = set()
    tried.add("11111111")

    while Ni != 0:
        L = nb_ones * ["1"] + (8 - nb_ones) * ["0"]
        while "".join(L) in tried:  # shuffle
            for i in range(7, 0, -1):
                j = np.random.randint(0, i+1)
                L[i], L[j] = L[j], L[i]
        s = "".join(L)
        tried.add(s)
        # print(s, flush=True)
        custom_output(s)
        Ni = int(input())

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        process()
