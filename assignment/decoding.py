def charToInt(digit):
    return chr(digit + 96)   # 1 -> 'a', 2 -> 'b', ...

def f(s):
    # base case
    if len(s) == 0:
        return [""]
    if s[0] == '0':   # invalid code
        return []

    results = []

    # case1: take one digit
    digit1 = int(s[0])
    char1 = charToInt(digit1)
    subResults1 = f(s[1:])
    for sub in subResults1:
        results.append(char1 + sub)

    # case2: take two digits
    if len(s) >= 2:
        digit2 = int(s[0] + s[1])
        if 10 <= digit2 <= 26:
            char2 = charToInt(digit2)
            subResults2 = f(s[2:])
            for sub in subResults2:
                results.append(char2 + sub)

    return results


# main
s = input().strip()  # take string input
res = f(s)
print("[" + ", ".join(res) + "]")

