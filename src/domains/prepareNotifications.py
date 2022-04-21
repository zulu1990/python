
# Get Box review files
# Check items to send notifications
# Prepare notification artifact
# Update excel status for the items
# Send notifications??
import json
import logging
from models.Parameters import Parameters
from services.boxService import BoxService
from services.excelService import ExcelService
from services.fileService import clear_folder

logger = logging.getLogger(__name__)

def process_notification(params: Parameters):
    try:
        box_service = BoxService()
        excel_service = ExcelService()

        box_files = box_service.download_reports(params.ReportSubPath)
        feedback_files = excel_service.prepare_notifications_file(box_files, params)
        json_data = json.dumps(feedback_files)
        test_value = 'defined inside python'
        print("json data {0}".format(json_data))
        print(r'##vso[task.setvariable variable=json_data]{0}'.format(json_data))
        print(r'##vso[task.setvariable variable=test_value]{0}'.format(json_data))

    except BaseException as bs:
        print(bs)

def process_finish(params: Parameters):
    box_service = BoxService()
    excel_service = ExcelService()
    print('asdasd', params.feedback_files)
    feedback_files = json.loads(params.feedback_files)
    
    feedback_delivered = feedback_files 
    
    print('asdasd', feedback_delivered)

    excel_service.complete_send_feedback(feedback_delivered, params)
    box_service.update_contents_to_box(feedback_files, params.ReportSubPath)

    # clear_folder(params.ReportSubPath)
    # clear_folder(params.NotificationSubPath)