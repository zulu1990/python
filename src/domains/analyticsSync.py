from config import AppInsightsConfig, PathsConfig
from models.Parameters import Parameters
from services.boxService import BoxService
from services.excelService import ExcelService
from services.fileService import get_last_record_date, clear_folder


def process_analytics_sync(params: Parameters):
    excel_client = ExcelService()
    box_client = BoxService()

    # Get Excel Data
    last_report_id = box_client.download_report(params.ReportSubPath)
    last_record_date = get_last_record_date(PathsConfig, sub_path=params.ReportSubPath, work_sheet=params.WorkSheet)

    # Get Analytics
    res = excel_client.get_application_insights_data(AppInsightsConfig, last_record_date, params.FeedbackQuery)

    # Update excel file
    status = excel_client.prepare_excel(res, PathsConfig, params)
    box_client.update_box_folder(status, last_report_id, params.ReportSubPath)
    clear_folder(params.ReportSubPath)
