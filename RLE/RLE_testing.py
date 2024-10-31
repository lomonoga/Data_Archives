import os

from evaluate_compression.evaluate_compression_from_files import evaluate_compression_from_files


def test(directory_path: str):
    input_directory_path = directory_path + '/input_files'
    output_directory_path = directory_path + '/output_files'

    if not os.path.exists(input_directory_path):
        print(f'Каталог {input_directory_path} не найден.')
        return

    for filename in os.listdir(input_directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                from RLE import RLE
                print(f'Обработка файла: {filename}')

                # Применяем RLE к каждой строке
                compressed_lines = [RLE.rle_encode(line.strip()) for line in file]

                # Сохранение сжатого файла
                compressed_file_path = os.path.join(output_directory_path, f'encoded_RLE_{filename}')
                with open(compressed_file_path, 'w', encoding='utf-8') as compressed_file:
                    for compressed_line in compressed_lines:
                        compressed_file.write(compressed_line + '\n')

                print(f'Сжатый файл сохранен как: {compressed_file_path}')

                # Разжатие сжатого файла и сохранение результата
                decompressed_lines = [RLE.rle_decode(line.strip()) for line in compressed_lines]
                decompressed_file_path = os.path.join(output_directory_path, f"decompressed_RLE_{filename}")
                with open(decompressed_file_path, 'w', encoding='utf-8') as decompressed_file:
                    for decompressed_line in decompressed_lines:
                        decompressed_file.write(decompressed_line + "\n")

                print(f"Разжатый файл сохранен как: {decompressed_file_path}")

                compression_ratio, compression_rate = evaluate_compression_from_files(
                    original_file_path=file_path,
                    compressed_file_path=compressed_file_path
                )
                print("Compression Ratio:", compression_ratio)
                print("Compression Rate:", compression_rate, '\n')
