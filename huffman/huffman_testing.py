import os

from huffman.huffman import huffman_decoding, huffman_encoding
from evaluate_compression.evaluate_compression_from_files import evaluate_compression_from_files


def test(directory_path: str):
    input_directory_path = os.path.join(directory_path, 'input_files')
    output_directory_path = os.path.join(directory_path, 'output_files')

    if not os.path.exists(input_directory_path):
        print(f'Каталог {input_directory_path} не найден.')
        return

    if not os.path.exists(output_directory_path):
        os.makedirs(output_directory_path)

    for filename in os.listdir(input_directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                print(f'Обработка файла: {filename}\n')

                original_text = file.read()

                encoded_data, huffman_codes = huffman_encoding(original_text)

                compressed_file_path = os.path.join(output_directory_path,
                                                    f'encoded_huffman_{os.path.splitext(filename)[0]}.bin')
                with open(compressed_file_path, 'wb') as compressed_file:
                    compressed_file.write(encoded_data)

                print(f'Сжатый файл сохранен как: {compressed_file_path}')

                with open(compressed_file_path, 'rb') as compressed_file:
                    encoded_data_from_file = compressed_file.read()

                decoded_text = huffman_decoding(encoded_data_from_file, huffman_codes)

                decompressed_file_path = os.path.join(output_directory_path,
                                                      f'decoded_huffman_{os.path.splitext(filename)[0]}.txt')
                with open(decompressed_file_path, 'w', encoding='utf-8') as decompressed_file:
                    decompressed_file.write(decoded_text)

                print(f'Разжатый файл сохранен как: {decompressed_file_path}')

                compression_ratio, compression_rate = evaluate_compression_from_files(
                    original_file_path=file_path,
                    compressed_file_path=compressed_file_path
                )
                print("Compression Ratio:", compression_ratio)
                print("Compression Rate:", compression_rate, '\n')
