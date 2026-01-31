import os
import sys
from pathlib import Path

def sort_files(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("❌ Указана неверная папка")
        return

    files = [f for f in folder.iterdir() if f.is_file()]
    if not files:
        print("📂 В папке нет файлов для сортировки")
        return

    for file in files:
        ext = file.suffix.lower().replace('.', '')
        if not ext:
            ext = 'no_extension'

        target_dir = folder / ext
        target_dir.mkdir(exist_ok=True)

        file.rename(target_dir / file.name)

    print("✅ Готово! Файлы отсортированы по расширениям.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python3 sorter.py /path/to/folder")
    else:
        sort_files(sys.argv[1])
