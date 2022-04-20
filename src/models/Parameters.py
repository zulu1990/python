from enum import Enum, auto


class Parameters:
    def __init__(self):
        self.FormulaRange = None
        self.Formula = None
        self.FeedbackCompleteMark = None
        self.FeedbackSendMark = None
        self.WorkSheet = None
        self.ReportSubPath = None
        self.FeedbackQuery = None
        self.ReportTemplate = None
        self.NotificationTemplate = None
        self.NotificationSubPath = ''
        self.NotificationList = ''
        self.Execute = None
        self.feedback_files = []

    def set_parameters(self, args: any):
        self.Execute = Execute[f'{args.execute}']
        self.NotificationSubPath = args.notification_sub_path
        self.NotificationTemplate = args.notification_template
        self.ReportTemplate = args.report_template
        self.FeedbackQuery = args.feedback_query
        self.ReportSubPath = args.report_sub_path
        self.WorkSheet = args.work_sheet
        self.FeedbackSendMark = args.feedback_send_mark
        self.FeedbackCompleteMark = args.feedback_complete_mark
        self.Formula = args.formula
        self.FormulaRange = args.formula_range
        self.NotificationList = self.NotificationSubPath + self.NotificationTemplate
        self.feedback_files = args.feedback_files


class Execute(Enum):
    ANALYTIC = auto()
    NOTIFICATION = auto()
    CUSTOM = auto()
