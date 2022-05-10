from argparse import ArgumentParser

from models.Parameters import Parameters


def parse_parameters():
    parser = ArgumentParser()

    parser.add_argument('--execute', help='determines which part of application to run', type=str, default='ANALYTIC')
    parser.add_argument('--feedback_files', help='sent feedback list', type=str, default='')
    parser.add_argument('--notification_template', help='notification template file name', type=str, default='notification_template.xlsx')
    parser.add_argument('--report_template', help='report template file name', type=str, default='report_template.xlsx')
    parser.add_argument('--feedback_query', help='feedback query function name', type=str, default= 'GetUserFeedbacksAutomation()')
    parser.add_argument('--report_sub_path', help='reports folder sub path', type=str, default='reports/')
    parser.add_argument('--notification_sub_path', help='notification folder sub path', type=str, default='notifications/')
    parser.add_argument('--work_sheet', help='working sheet name', type=str, default='Sheet1')
    parser.add_argument('--feedback_send_mark', help='mark which indicates to send feedback', type=str, default='send_feedback')
    parser.add_argument('--feedback_complete_mark', help='mark which indicates feedback was sent', type=str, default='completed_feedback_sent')
    parser.add_argument('--formula', help='excel formula to validate statuses', type=str, default='=fields!$A$2:$A$9')
    parser.add_argument('--formula_range', help='column range to apply --formula', type=str, default='A2:A1048576')
    
    
    params = Parameters()
    args = parser.parse_args()

    print(f"in args, {args.feedback_files}")
    params.set_parameters(args)

    return params
