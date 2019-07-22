import random

message = 'Hello World'
maskList = [1, 2, 4, 8, 16, 32, 64]
bitPosition = [0, 6, 13, 22, 27, 28, 31, 1, 4, 8, 17, 25, 26, 30, 3, 7, 8, 9, 15, 24, 26]
encoded = []
temp = [2554339393, 1174536466, 83919752]
charCount = 0
offset = 0
while charCount < len(message):
    char = message[charCount]
    print(char)
    print("{0:b}".format(ord(char)))
    encoded.append(random.randint(0, 2140000000))

    if offset > 14:
        offset = 0

    for i in range(0, 7):
        if ord(char) & maskList[i]:
            encoded[charCount] |= 1 << bitPosition[i+offset]
        else:
            encoded[charCount] &= ~(1 << bitPosition[i+offset])

    print("{0:032b}".format(encoded[charCount]))
    if offset < 7:
        print("{0:032b}".format(temp[0]))
    elif offset < 14:
        print("{0:032b}".format(temp[1]))
    else:
        print("{0:032b}".format(temp[2]))
    charCount += 1
    offset += 7

print(encoded)