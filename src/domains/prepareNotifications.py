
# Get Box review files
# Check items to send notifications
# Prepare notification artifact
# Update excel status for the items
# Send notifications??
from models.Parameters import Parameters
from services.boxService import BoxService
from services.excelService import ExcelService
from services.fileService import clear_folder


def process_notification(params: Parameters):
    box_service = BoxService()
    excel_service = ExcelService()

    box_files = box_service.download_reports(params.ReportSubPath)
    feedback_files = excel_service.prepare_notifications_file(box_files, params)
    print(feedback_files)

def process_finish(params: Parameters):
    box_service = BoxService()
    excel_service = ExcelService()

    # feedback_delivered = send_notification()
    feedback_files = params.feedback_files
    feedback_delivered = feedback_files
    excel_service.complete_send_feedback(feedback_delivered, params)
    box_service.update_contents_to_box(feedback_files, params.ReportSubPath)

    # clear_folder(params.ReportSubPath)
    # clear_folder(params.NotificationSubPath)