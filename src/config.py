
import logging
import os
import sys

Log_Format = "%(levelname)s - %(message)s"

logging.basicConfig(format = Log_Format, 
                    level = logging.DEBUG)


class BoxAuthConfig:
    """Configuration object container JWT auth"""
    CLIENT_ID = os.getenv('BOX_CLIENT_ID', "fwofs5712yvq0eo17fpo9vyk7iqiorc1")
    CLIENT_SECRET = os.getenv('BOX_CLIENT_SECRET', "AY8SdZrAwvpr7flUhffZXnNlhduiMuGK")
    ENTERPRISE_ID = os.getenv('BOX_ENTERPRISE_ID')
    JWT_KEY_ID = os.getenv('BOX_JWT_KEY_ID')
    CERT_KEY_PATH = os.getenv('BOX_CERT_KEY_PATH')
    CERT_KEY_PASSPHRASE = os.environ.get('BOX_CERT_KEY_PASSPHRASE')
    DEVELOPER_TOKEN = os.getenv("BOX_DEVELOPER_TOKEN", "axtMBoXuzh70NGYEX4ZAbop3GzW8XG3N")
    FOLDER_ID = os.getenv("BOX_FOLDER_ID", "159813753976")
    #dont commit this
class AppInsightsConfig:
    """Configuration object container for """
    AZURE_APPLICATION_INSIGHTS_KEY = os.getenv('AZURE_APPLICATION_INSIGHTS_KEY')
    AZURE_APPLICATION_INSIGHTS_ID = os.getenv('AZURE_APPLICATION_INSIGHTS_ID')
    AZURE_APPLICATION_INSIGHTS_BASE_URL = os.getenv('AZURE_APPLICATION_INSIGHTS_BASE_URL',
                                                    'https://api.applicationinsights.io/v1/apps')

#dont commit this

class PathsConfig:
    """Configuration object container for paths"""
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    BOX_FOLDER_NAME = os.getenv('BOX_FOLDER_NAME', 'Sophia')
    LOCAL_FILE_PATH = os.getenv('LOCAL_FILE_PATH', 'data/')
    TEMPLATE_FILE_PATH = os.getenv('TEMPLATE_FILE_PATH', 'data/templates/')

#dont commit this