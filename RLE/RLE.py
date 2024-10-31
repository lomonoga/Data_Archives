def rle_encode(data: str):
    encoding = ""
    i = 0

    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        encoding += data[i] + str(count)
        i += 1

    return encoding


def rle_decode(data: str):
    decoding = ""
    i = 0

    while i < len(data):
        char = data[i]
        i += 1
        count = ""
        while i < len(data) and data[i].isdigit():
            count += data[i]
            i += 1
        decoding += char * int(count)

    return decoding
