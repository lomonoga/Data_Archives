import heapq


def huffman_encoding(data):
    key = dict()
    encoded = str()
    corp = dict()

    # Подсчет частоты символов
    for char in data:
        corp[char] = corp.get(char, 0) + 1

    htree = [[weight, [char, ""]] for char, weight in corp.items()]
    heapq.heapify(htree)

    while len(htree) > 1:
        left_node = heapq.heappop(htree)
        right_node = heapq.heappop(htree)
        for char in left_node[1]:
            key[char] = '0' + key.get(char, "")
        for char in right_node[1]:
            key[char] = '1' + key.get(char, "")
        heapq.heappush(htree, [left_node[0] + right_node[0], left_node[1] + right_node[1]])

    # Замена всех символов их битовыми кодами
    for char in data:
        encoded += key[char]

    # Заполняем оставшиеся биты нулями
    rem = len(encoded) % 8
    key['rem'] = rem
    encoded += '0' * rem

    # Преобразование строки бит в байты
    byte_array = bytearray()
    for i in range(0, len(encoded), 8):
        byte_array.append(int(encoded[i:i + 8], 2))

    return byte_array, key


def huffman_decoding(encoded, key):
    reverse_key = {v: k for k, v in key.items()}
    decoded = ""
    current_code = ""

    for byte in encoded:
        bits = format(byte, '08b')  # Преобразуем байт в строку бит
        for bit in bits:
            current_code += bit
            if current_code in reverse_key:
                decoded += reverse_key[current_code]
                current_code = ""

    return decoded
