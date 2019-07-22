import random

encodeMasks = [1, 2, 4, 8, 16, 32, 64]
encodeBitPositions = [0, 6, 13, 22, 27, 28, 31, 1, 4, 8, 17, 25, 26, 30, 3, 7, 8, 9, 15, 24, 26]
decodeMasks = [[1, 64, 8192, 4194304, 134217728, 268435456, 2147483648], [2, 16, 256, 131072, 33554432, 67108864, 1073741824], [8, 128, 256, 512, 32768, 16777216, 67108864]]
debugBitPositions = [2554339393, 1174536466, 83919752]
DEBUG = False


def encode(message):
    encoded = []
    charCount = 0
    offset = 0

    while charCount < len(message):
        char = message[charCount]
        encoded.append(random.randint(0, 2140000000))

        if offset > 14:
            offset = 0

        for i in range(0, 7):
            if ord(char) & encodeMasks[i]:
                encoded[charCount] |= 1 << encodeBitPositions[i + offset]
            else:
                encoded[charCount] &= ~(1 << encodeBitPositions[i + offset])

        if DEBUG:
            print(char)
            print("{0:b}".format(ord(char)))
            print("{0:032b}".format(encoded[charCount]))
            if offset < 7:
                print("{0:032b}".format(debugBitPositions[0]))
            elif offset < 14:
                print("{0:032b}".format(debugBitPositions[1]))
            else:
                print("{0:032b}".format(debugBitPositions[2]))

        charCount += 1
        offset += 7

    if DEBUG:
        print(encoded)

    return encoded


def decode(binary):
    decodedMessage = ''
    offset = 0

    for bytes in binary:

        if offset > 2:
            offset = 0
        out = 0
        for i in range(0, 7):
            if bytes & decodeMasks[offset][i]:
                out |= 1 << i

        decodedMessage += chr(out)
        offset += 1

    print(decodedMessage)


def intermediate(binary):
    crypticMessage = ""
    for encoded in binary:
        bytes = "{0:032b}".format(encoded)

        crypticMessage += chr(int(bytes[0:8], 2) % 95+32)
        crypticMessage += chr(int(bytes[8:16], 2) % 95+32)
        crypticMessage += chr(int(bytes[16:24], 2) % 95+32)
        crypticMessage += chr(int(bytes[24:32], 2) % 95+32)

    print(crypticMessage)


stuff = []
data = 'I like to eat apples and bananas. Should I have posted this on this fifth world reddit page? I have no Idea but I did it anyways'
print("BEFORE -> " + data)
stuff = encode(data)
print("INBETWEEN ->")
intermediate(stuff)
print("AFTER -> ")
decode(stuff)
