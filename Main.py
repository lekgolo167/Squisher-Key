
message = 'Hello World'

for char in message:
    print(char)
    print("{0:b}".format(ord(char)))
    mask = 0
    if (ord(char)&1):
        mask |= 1 << 1
    if (ord(char)&2):
        mask |= 1 << 2
    if (ord(char)&4):
        mask |= 1 << 3
    if (ord(char)&8):
        mask |= 1 << 4
    if (ord(char)&16):
        mask |= 1 << 5
    if (ord(char)&32):
        mask |= 1 << 6
    if (ord(char)&64):
        mask |= 1 << 7

    print("{0:b}".format(mask))
