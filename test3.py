def solution(riddle):
    riddle = 'e' + riddle + 'f'
    r = list(riddle)
    string = ""
    lr = len(r) - 1
    for i in range(1, lr):
        if r[i] == '?':
            x = ord(r[i - 1]) + 1
            y = ord(r[i + 1])
            if x == y:
                string = string + chr(x + 2)
                r[i] = chr(x + 2)

            elif chr(x) == 'z' and x == y:
                string = string + 'a'
                r[i] = 'a'
            else:
                string = string + chr(x)
                r[i] = chr(x)
        else:
            string = string + r[i]
    return string
    pass
