from settings import configGeneral
from selenium import webdriver
from castro import Castro
import os
from multiprocessing import Process, freeze_support
import time

video = Castro()


# Todo: mejorar el proceso de grabar archivos en una carpeta por ejecucion
def takeScreenshot(driver, pathname=None):
    file_name = "\\screen_" + time.strftime("%d_%m_%y_%H_%M_%S") + ".png"
    if not pathname:
        path = configGeneral.get_report_path()
        if not path:
            defaultpath = os.path.join(os.path.dirname(__file__), "..\\..\\reports")
            path = defaultpath
    else:
        path = pathname

    driver.save_screenshot(path + file_name)
    #Evito que dos archivos se generen en la misma hora
    time.sleep(1)


# TODO: pendiente resolver el problema de multithread
def startVideoRecorder(environment):
    if environment == '__main__':
        freeze_support()
        Process(target=video.start()).start()


# TODO: pendiente resolver el problema de multithread
def stopVideoRecorder():
    video.stop()
    video.process()