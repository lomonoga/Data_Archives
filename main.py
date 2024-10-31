from RLE import RLE_testing
from huffman import huffman_testing


def test_archivers(name_archive: str) -> ():
    directory_path = './all_files/txt_files'
    match name_archive.lower():
        case "rle":
            RLE_testing.test(directory_path)
        case "huffman":
            huffman_testing.test(directory_path)
        case _:
            print('Извините, но такого алгоритма ещё не реализованно(')


if __name__ == '__main__':
    input_name = input('Введите название архивации:\n')
    print('\n')
    test_archivers(name_archive=input_name)
