from utils.selenium_utils import SeleniumConnections
import logging

def before_all(context):
    print ("entro")
    logging.info("entro")
    context.driver = SeleniumConnections.connect(10)


def after_all(context):
    context.driver.quit()
    logging.info("salio")
    print ("salio")