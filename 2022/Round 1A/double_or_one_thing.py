def doubleOrOne():
    s = input()
    n = len(s)
    newS = []
    i = 0
    while i < (n-1):
        si = s[i]
        if si < s[i+1]:
            newS.extend(2 * [si])
            i += 1
        elif (si == s[i+1]):
            for j in range(i+2, n):
                if s[j] != s[j-1]:
                    break
            if s[j] != s[j-1]:
                if s[j] > si:
                    newS.extend((2 * (j - i)) * [si])
                else:
                    newS.extend((j - i) * [si])
            else:
                newS.extend((j - i) * [si])
            i = j
        else:
            newS.append(si)
            i += 1

    newS.append(s[n-1])
    return "".join(newS)

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        print(f'Case #{case}: {doubleOrOne()}')
