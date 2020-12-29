import requests
import os
import zipfile
from collections import defaultdict

keep_files = {'.gitkeep'}

for f in os.listdir('data'):
    if f not in keep_files:
        os.remove(f'data/{f}')

links = [
    'https://resources.oreilly.com/conferences/'
    'natural-language-processing-with-deep-learning/raw/master/data/glove.6B.100d.txt']


def unzip(archive_path) -> None:
    zipfile.ZipFile(archive_path).extractall(path='data')
    os.remove(archive_path)


def plane_file(_) -> None:
    pass


file_type_extractors = defaultdict(lambda: plane_file)
file_type_extractors['.zip'] = unzip

for link in links:
    file_name = os.path.basename(link)
    extension = os.path.splitext(file_name)[1]

    response = requests.get(link)

    save_path = f'data/{file_name}'
    with open(save_path, 'wb') as f:
        f.write(response.content)
    file_type_extractors[extension](save_path)
