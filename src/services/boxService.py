import logging
import os
from datetime import date

from boxsdk import OAuth2, Client

from config import BoxAuthConfig, PathsConfig
from models.BoxFile import BoxFile
from services.fileService import get_file_name


def init_box_client(config: BoxAuthConfig):

    auth = OAuth2(
        client_id=config.CLIENT_ID,
        client_secret=config.CLIENT_SECRET,
        access_token=config.DEVELOPER_TOKEN
    )
    return Client(auth)


class BoxService:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.client = init_box_client(BoxAuthConfig)
        self.logger.info(f'creds: {BoxAuthConfig.CLIENT_ID}, {BoxAuthConfig.CLIENT_SECRET}, {BoxAuthConfig.DEVELOPER_TOKEN}')

    def download_report(self, sub_path: str):
        box_files = self.client.folder(BoxAuthConfig.FOLDER_ID).get_items()
        last_item = [file for file in box_files][-1]

        output = open(PathsConfig.LOCAL_FILE_PATH + sub_path + last_item.name, 'wb')
        self.client.file(last_item.id).download_to(output)
        self.logger.info('file downloaded')
        return last_item.id

    def download_reports(self, sub_path: str):
        try:
            box_files = self.client.folder(BoxAuthConfig.FOLDER_ID).get_items()
            items = [report for report in box_files]
            file_list = []
            for item in items:
                output = open(PathsConfig.LOCAL_FILE_PATH + sub_path + item.name, 'wb')
                self.client.file(item.id).download_to(output)
                file_list.append(BoxFile(item.id, item.name))

            return file_list
        except BaseException as exc:
            self.logger.error(f'error occurred while downloading reports {exc}')

    def upload_file(self, file_path: str):
        self.client.folder(BoxAuthConfig.FOLDER_ID).upload(file_path=file_path)

    def update_content(self, file_path: str, file_id: str):
        self.client.file(file_id).update_contents(file_path)

    def update_box_folder(self, status, last_report_id: str, sub_path: str):
        prev_month_updated = status[0]
        cur_month_updated = status[1]
        cur_month_created = status[2]
        this_month = date.today().month
        path = PathsConfig.LOCAL_FILE_PATH + sub_path

        if prev_month_updated:
            file = path + get_file_name(month=this_month-1)
            self.update_content(file, last_report_id)
        elif cur_month_updated:
            file = path + get_file_name()
            self.update_content(file, last_report_id)

        if cur_month_created:
            file = path + get_file_name()
            self.upload_file(file)

    def update_contents_to_box(self, files, sub_path: str):
        folder = PathsConfig.LOCAL_FILE_PATH + sub_path
        for item in files:
            print("item", item)
            file_path = folder + item['FileName']
            self.update_content(file_path, item.FileId)


