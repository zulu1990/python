import os

from domains.analyticsSync import process_analytics_sync
from domains.prepareNotifications import process_notification
from models.Parameters import Execute
from services.parametersService import parse_parameters

if __name__ == '__main__':
    params = parse_parameters()

    # parse arguments ??
    # make it work as a CLI
    #
    # api: python training-center --prepareUserReviewNotifications
    # api: python training-center --syncAnalytics
    # api: python training-center --extractAutomationTestsExamples
    if params.Execute == Execute.ANALYTIC:
        process_analytics_sync(params)
    elif params.Execute == Execute.NOTIFICATION:
        process_notification(params)
