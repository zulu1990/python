from boxsdk import Client, JWTAuth
from boxsdk import OAuth2, Client

from configuration.config import BoxConfig

data_path = './data/'


def init_box_client(config: BoxConfig):
    auth = OAuth2(
        client_id=config.CLIENT_ID,
        client_secret=config.CLIENT_SECRET,
        access_token=config.DEVELOPER_TOKEN,
    )
    client = Client(auth)

    return client


class BoxService:
    def __init__(self):
        self.client = init_box_client(BoxConfig)

    def download_file(self):
        box_files = self.client.folder(BoxConfig.FOLDER_ID).get_items()
        last_item = [asd for asd in box_files][-1]

        output = open(last_item.name, 'wb')
        self.client.file(last_item.id).download_to(output)
        return last_item.id

    def download_files(self):
        try:
            box_files = self.client.folder(BoxConfig.FOLDER_ID).get_items()
            items = [report for report in box_files]

            file_list = []
            for item in items:
                output = open(data_path + 'reports/' + item.name, 'wb')
                self.client.file(item.id).download_to(output)
                file_list.append({'file_id': item.id, 'file_name': item.name})

            return file_list
        except BaseException as ex:
            print(ex)

    def update_content(self, file_path: str, file_id: str):
        self.client.file(file_id).update_contents(file_path)

    def upload_new_file(self, file_path: str):
        self.client.folder(BoxConfig.FOLDER_ID).upload(file_path=file_path)
