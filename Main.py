
message = 'Hello World'
maskList = [0, 1, 2, 4, 8, 16, 32, 64]
bitPosition = [0, 8, 16, 24, 32, 39, 47, 54, 61, 68, 75, 81, 87, 93, 98, 103, 107, 111, 115, 118, 121, 123, 125, 126, 127]
charCount = 0
while charCount < len(message):
    char = message[charCount]
    print(char)
    print("{0:b}".format(ord(char)))
    encoded = 0
    maskCount = 0

    for i in range(0, len(bitPosition)):
        if maskCount > 7:
            maskCount = 0
            charCount += 1
            char = message[charCount]

        if ord(char) & maskList[maskCount]:
            encoded |= 1 << maskCount
        else:
            encoded |= 0 << maskCount

        maskCount += 1

    print("{0:b}".format(encoded))
