from os.path import abspath

from capabilities import select_capabilities, start_session
from pages.android.commom_page import CommomPage


def before_all(context):
    context.app_path = context.config.userdata['app_path']
    context.environment = context.config.userdata['environment']
    context.device_name = context.config.userdata['device_name']
    context.os_version = context.config.userdata['os_version']
    context.browserstack = context.config.userdata.getbool('browserstack')
    context.appium_url = context.config.userdata['appium_url']
    context.abs_app_path = abspath(context.app_path)

    capabilities_template = select_capabilities(context.browserstack)
    context.driver = start_session(
        context.appium_url,
        capabilities_template(
            context.abs_app_path,
            context.device_name,
            context.os_version
        )
    )


def before_feature(context, feature):
    pass


def before_step(context, step):
    context.driver.implicitly_wait(5) 


def after_step(context, step):
    pass


def after_feature(context, feature):
    pass


def after_all(context):
    context.driver.quit()
