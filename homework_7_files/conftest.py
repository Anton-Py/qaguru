from homework_7_files.const import DATA_DIR
from zipfile import ZipFile
import os.path
import pytest


def check_and_remove_archive(directory):
    archive_path = os.path.join(directory, 'big_archives.zip')

    if os.path.exists(archive_path):
        print(f"Архив {archive_path} уже существует и будет удален.")
        os.remove(archive_path)
    # else:
    #     print(f"Архив {archive_path} не существует. Он будет создан.")


@pytest.fixture(scope='session')
def create_archive():
    archives_path = os.path.join(DATA_DIR, "big_archives.zip")

    with ZipFile(archives_path, "w") as zip_file:
        names = ['file_example_XLSX_50.xlsx', 'users.csv', 'КП_выпускные_2025.pdf']
        for arc_name in names:
            file_to_add = os.path.join(DATA_DIR, arc_name)
            zip_file.write(file_to_add, arcname=arc_name)  # добавляем файл в архив


    yield archives_path

    check_and_remove_archive(DATA_DIR)