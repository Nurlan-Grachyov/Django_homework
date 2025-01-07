import subprocess
import chardet


def create_fixture():
    subprocess.run(['python', 'manage.py', 'dumpdata', 'catalog.Product', 'catalog.Category', '--indent', '2', '>',
                    'new_fixture.json'], shell=True)

    with open('new_fixture.json', 'rb') as source_file:
        raw_data = source_file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    with open('new_fixture.json', 'r', encoding=encoding) as source_file:
        data = source_file.read()

    with open('new_fixture_utf8.json', 'w', encoding='utf-8') as target_file:
        target_file.write(data)
