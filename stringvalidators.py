if __name__ == '__main__':
    s = raw_input()
    reisalnum = False
    reisalpha = False
    reisdigit = False
    reislower = False
    reisupper = False
    if any(map(str.isalnum,s)):
        reisalnum = True
    if any(map(str.isalpha,s)):
        reisalpha = True
    if any(map(str.isdigit,s)):
        reisdigit = True
    if any(map(str.islower,s)):
        reislower = True
    if any(map(str.isupper,s)):
        reisupper = True
    
    print reisalnum
    print reisalpha
    print reisdigit
    print reislower
    print reisupper
