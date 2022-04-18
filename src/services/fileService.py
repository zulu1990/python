from datetime import datetime, date
from os import listdir, remove
from os.path import exists

import pandas as pd

from config import PathsConfig


def get_file(path: str):
    today = date.today()
    file_name = get_file_name(today.year, today.month)
    file = path + file_name
    file_exists = exists(file)

    if not file_exists:
        file = path + get_file_name(today.year, today.month - 1)

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


def get_month_starter():
    return datetime.today().replace(day=1, hour=0, minute=0, second=0, microsecond=0)


def clear_folder(folder_sub_path: str):
    folder_path = PathsConfig.LOCAL_FILE_PATH + folder_sub_path
    for file in listdir(folder_path):
        remove(folder_path + file)
