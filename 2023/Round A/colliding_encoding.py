def main() -> str:
    encoding_list = input().split(" ")
    encoding = {chr(ord("A")+i): e for i, e in enumerate(encoding_list)}
    encoding[" "] = " "
    nb_word = int(input())
    s = set()
    i = 0
    res = None
    while (res is None) and (i < nb_word):
        i += 1
        encoded = "".join([encoding[c] for c in input()])
        if encoded in s:
            res = "YES"
        s.add(encoded)
    for _ in range(nb_word - i):
        _ = input()

    if res is None:
        res = "NO"
    return res
    
if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        print(f'Case #{case}: {main()}')
