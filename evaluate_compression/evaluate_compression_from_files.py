import os


def evaluate_compression_from_files(original_file_path, compressed_file_path):
    if not os.path.exists(original_file_path):
        print(f"Файл '{original_file_path}' не найден.")
        return
    if not os.path.exists(compressed_file_path):
        print(f"Файл '{compressed_file_path}' не найден.")
        return

    # Считываем размер оригинального и сжатого файлов в байтах
    original_size = os.path.getsize(original_file_path) * 8
    compressed_size = os.path.getsize(compressed_file_path) * 8

    # Вычисление коэффициента и эффективности сжатия
    compression_ratio = original_size / compressed_size
    compression_rate = 1 - (compressed_size / original_size)

    return compression_ratio, compression_rate
