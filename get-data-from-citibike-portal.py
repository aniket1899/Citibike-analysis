# import re
import requests
import sys
import curses

_URL = 'https://s3.amazonaws.com/tripdata/'
# _YEARS = ['2019', '2020', '2021', '2022']
_YEARS = ['2022']

_MONTHS = ['0'+str(m) if len(str(m)) < 2 else str(m) for m in list(range(1, 13)) ]
_STORAGE_PATH = 'data/'
def pbar(window):
    print('Downloading ... ')
    total_count = len(_MONTHS)*len(_YEARS)
    current = 1
    downloaded = 0
    for year in _YEARS:
        for month in _MONTHS:
            window.addstr(1, 1, f"Downloading ... {current}/{total_count}")
            window.addstr(5, 1, f"Completed ... {downloaded}/{total_count}")
            window.refresh()
            current += 1

            trailing_url = f'{year}{month}-citibike-tripdata.csv.zip'
            request = requests.get(_URL + trailing_url)
            if request.status_code == 404:
                continue
            tmp_fileloc = 'data/' + trailing_url
            with open(tmp_fileloc, 'wb') as f:
                f.write(request.content)
                f.close()
            downloaded += 1
    print('='*10)
    print(f'Total downloaded = {downloaded}/{total_count}')
    print('='*10)

curses.wrapper(pbar)

import zipfile
from os import listdir
from os.path import isfile, join

_ZIP_PATH = 'data/'
_UPZIP_PATH = 'data/data_unzipped/'
zip_file_names = [_ZIP_PATH+f for f in listdir(_ZIP_PATH) if isfile(join(_ZIP_PATH, f)) and '.zip' in f]
for zip_file_name in zip_file_names:
    with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
        zip_ref.extractall(_UPZIP_PATH)
print('Files unzipped and placed to target folder')