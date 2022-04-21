
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
        test_value = [{"FieldId": "941393029933", "FileName": "2022-3-Report.xlsx", "QuestionIds": []}, {"FieldId": "947082945940", "FileName": "2022-4-Report.xlsx", "QuestionIds": ["02910bf1b2d340df966539863f3c0cd6", "842045f395f947d8919edf66f4aefd50", "6748abae3aaa4727aa271d2a44043cc4", "5a3014ef3e6345e3884b1e85833d1ad9"]}]
        print("json data {0}".format(json_data))
        print('##vso[task.setvariable variable=json_data]{0}'.format(json_data))
        print('##vso[task.setvariable variable=test_value]{0}'.format(test_value))

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