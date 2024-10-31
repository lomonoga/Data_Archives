import RLE_testing


def test_archivers(name_archive: str) -> ():
    match name_archive.lower():
        case "rle":
            RLE_testing.test('./all_files/txt_files')
        case "huffman":
            ()


if __name__ == '__main__':
    input_name = input('Введите название архивации: ')
    test_archivers(name_archive=input_name)
