from os import getenv

from helpers.browserstack import upload_app


def capabilities_browserstack(app_path: str, device_name: str, os_version):
    """ 
    Returns capabilities to run a Browser Stack

    Args:
        - app_name: str - Name of the application you wanna run
        - device_name: str - Device you wanna run application
        - os_version: int - Version of Android you wanna run
    """
    browserstack_id = upload_app(app_path)
    return {
        'browserstack.user': getenv('browserstack_user'),
        'browserstack.key': getenv('browserstack_key'),
        'project': 'FeatureActivation',
        'build': 'Behave Android',
        'name': f'{app_path}',
        'browserstack.debug': False,
        'app': f"{browserstack_id['app_url']}",
        'device': 'Google Pixel 3',
        'os_version': os_version
    }
