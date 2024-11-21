from json import loads
from requests import post
from os import getenv
from os.path import abspath


def upload_app(app_path: str) -> dict:
    """
    Upload desired application to BrowserStack

    Args:
        - app_path: str - Path of application you wanna to upload

    Returns dict
    """
    with open(abspath(app_path), 'rb') as file:
        files = {
            'file': file
        }

        response = post(
            'https://api-cloud.browserstack.com/app-automate/upload',
            files=files,
            auth=(
                getenv('browserstack_user'),
                getenv('browserstack_key')
            )
        )
        return loads(response.text)
