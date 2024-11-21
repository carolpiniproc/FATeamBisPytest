def capabilities_emulator(app_path: str, device_name: str, os_version):
    """ 
    Returns capabilities to run a emulator in user computer
    
    Args:
        - app_name: str - Name of the application you wanna run
        - device_name: str - Device you wanna run application
        - os_version: int - Version of Android you wanna run
    """
    return {
        'platformName': 'Android',
        'platformVersion': os_version,
        'deviceName': device_name,
        'app': app_path,
        'automationName': 'UiAutomator2',
        'avd': device_name,
        'deviceReadyTimeout': 10,
    }
