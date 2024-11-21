from appium import webdriver
from appium.webdriver import Remote
from typing import Callable
from .android_browserstack import capabilities_browserstack
from .android_emulator import capabilities_emulator


def select_capabilities(browserstack_enabled: bool) -> Callable:
    """
    Select your capabilities based if you gonna run in
    browserstack

    Args:
        - browserstack_enabled: bool - Bool to represent run in
    browserstack

    Returns Callable
    """
    list_of_capabilities = {
        'browserstack': capabilities_browserstack,
        'emulator': capabilities_emulator
    }
    if browserstack_enabled:
        return list_of_capabilities['browserstack']
    return list_of_capabilities['emulator']


def start_session(appium_url: str, capabilities: dict) -> Remote:
    """
    Start appium session and return RemoteWebdriver

    Args:
        - appium_url: str - Url where Appium is running
        - capabilities: dict - Capabilities with the tests gonna run

    Returns Remote
    """
    return webdriver.Remote(
        command_executor=appium_url,
        desired_capabilities=capabilities
    )
