from datetime import datetime, date
from os import listdir, remove
from os.path import exists
from os.path import isfile, join
import pandas as pd

from config import PathsConfig


def get_file(path: str):
    downloaded_file = [f for f in listdir(path) if isfile(join(path, f))][-1]
    file = path + downloaded_file
    return file


def get_file_name(year: int = date.today().year, month: int = date.today().month,
                  verb: str = 'Report', extension: str = 'xlsx'):
    return f'{year}-{month}-{verb}.{extension}'


def get_last_record_date(paths: PathsConfig, sub_path: str, work_sheet: str):
    # at this point we already have the latest report from box.

    file = get_file(paths.LOCAL_FILE_PATH + sub_path)
    df = pd.read_excel(io=file, sheet_name=work_sheet)
    last_date = pd.to_datetime(df.timestamp.array[-1]) if not df.empty else get_month_starter()
    return last_date

def extract_date(file_name: str):
    print()


def get_month_starter(year: int = date.today().year, month: int = date.today().month):
    return datetime.today().replace(year=year, month=month, day=1, hour=0, minute=0, second=0, microsecond=0)


def clear_folder(folder_sub_path: str):
    folder_path = PathsConfig.LOCAL_FILE_PATH + folder_sub_path
    for file in listdir(folder_path):
        remove(folder_path + file)
