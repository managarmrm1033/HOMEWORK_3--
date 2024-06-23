import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor

def copy_file(src_path, dest_dir):
    # отримання розширення файлу
    file_extension = os.path.splitext(src_path)[1][1:]
    # Якщо розширення порожнє пропускаємо файл
    if not file_extension:
        return
    # Створити директорію для розширення якщо її нема
    dest_path = os.path.join(dest_dir, file_extension)
    os.makedirs(dest_path, exist_ok=True)
    # Скопіювати файл до директорії
    shutil.copy(src_path, dest_path)
    print(f"Copied: {src_path} to {dest_path}")

def process_directory(src_dir, dest_dir, executor):
    for root, _, files in os.walk(src_dir):
        for file in files:
            src_file_path = os.path.join(root, file)
            executor.submit(copy_file, src_file_path, dest_dir)

def main():
    src_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    with ThreadPoolExecutor() as executor:
        process_directory(src_dir, dest_dir, executor)

if __name__ == "__main__":
    main()
