from configuration.config import BoxConfig
from services.boxService import BoxService
from services.excelWorker import crete_excel_file_from_template, process_files

if __name__ == '__main__':
    # crete_excel_file_from_template()
    boxService = BoxService()
    # file_id = boxService.download_file()
    # boxService.update_content('2022-03-Report.xlsx', file_id)
    files = boxService.download_files()
    process_files(files)
