"""
def tower():
    n = int(input())
    towers = []
    for _ in range(n):
        towers.append(list(map(int, input().split(" "))))

    is_valid = True
    i = 0
    while is_valid and (i < n):
        s = set()
        s.add(towers[i][0])
        for j in range(1, len(towers[i])):
            if towers[i][j] != towers[i][j-1]:  # new letter
                if towers[i][j] in s:  # already seen before!
                    is_valid = False
                    break
                else:
                    s.add(towers[i][j])
        i += 1
    
    i = 0
    total_middle_letters = set()
    while is_valid and (i < n):
        middle_letters = set()
        for j in range(1, len(towers[i])-1):
            if (towers[i][j] != towers[i][0]) and (towers[i][j] != towers[i][-1]) and (towers[i][j] in total_middle_letters):
                is_valid = False
                break
            else:
                middle_letters.add(j)
        total_middle_letters = total_middle_letters.union(middle_letters)

    # if one tower is invalid
    if not(is_valid):
        return "IMPOSSIBLE"
    
    first_letters = {}
    last_letters = {}
    for i, t in enumerate(towers):
        fl = t[0]
        ll = t[-1]
        if fl in first_letters:
            first_letters[fl] = [i]
        else:
            first_letters[fl].append(i)
        if ll in last_letters:
            last_letters[ll] = [i]
        else:
            last_letters[ll].append(i)
    
    # find the first word (don't match with end of another word)
    root = 0
    while (root < n) and (towers[root][0] in last_letters):
        root += 1
    if root == n:
        return "IMPOSSIBLE"

    graph = [[] for _ in range(n)]
    for fl in first_letters:
        L = first_letters[fl]
        L2 = last_letters.get(fl, [])
        for i in L:
            for j in L2:
                if i != j:
                    graph[i].append(j)
    for ll in last_letters:
        L = last_letters[ll]
        L2 = first_letters.get(ll, [])
        for i in L:
            for j in L2:
                if i != j:
                    graph[i].append(j)
"""
from itertools import permutations
def tower():
    n = int(input())
    towers = list(map(str, input().split(" ")))
    
    is_valid = True
    i = 0
    while is_valid and (i < n):
        s = set()
        s.add(towers[i][0])
        for j in range(1, len(towers[i])):
            if towers[i][j] != towers[i][j-1]:  # new letter
                if towers[i][j] in s:  # already seen before!
                    is_valid = False
                    break
                else:
                    s.add(towers[i][j])
        i += 1
    
    if not(is_valid):
        return "IMPOSSIBLE"
    
    i = 0
    total_middle_letters = set()
    while is_valid and (i < n):
        middle_letters = set()
        for j in range(1, len(towers[i])-1):
            if (towers[i][j] != towers[i][0]) and (towers[i][j] != towers[i][-1]) and (towers[i][j] in total_middle_letters):
                is_valid = False
                break
            else:
                middle_letters.add(j)
        total_middle_letters = total_middle_letters.union(middle_letters)
        i += 1

    if not(is_valid):
        return "IMPOSSIBLE"

    for w in permutations(towers, n):
        word = "".join(w)
        word_len = len(word)
        is_valid = True
        i = 0
        while is_valid and (i < word_len):
            s = set()
            s.add(word[0])
            for j in range(1, word_len):
                if word[j] != word[j-1]:  # new letter
                    if word[j] in s:  # already seen before!
                        is_valid = False
                        break
                    else:
                        s.add(word[j])
            i += 1
        if is_valid:
            return word
    
    return "IMPOSSIBLE"
    

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        print(f'Case #{case}: {tower()}')
