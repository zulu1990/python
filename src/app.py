import logging
import os

from domains.analyticsSync import process_analytics_sync
from domains.prepareNotifications import process_notification, process_finish
from models.Parameters import Execute
from services.parametersService import parse_parameters

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    params = parse_parameters()

    logger.info(f"log information {params.Execute}")
    logger.error(f"log error {params.Formula}")

    if params.Execute == Execute.ANALYTIC:
        process_analytics_sync(params)
    elif params.Execute == Execute.NOTIFICATION:
        process_notification(params)
    elif params.Execute == Execute.CUSTOM:
        process_finish(params)