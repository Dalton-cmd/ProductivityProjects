import os
from os import listdir
import random
from os.path import isfile, join
import datetime, time, ctypes, sys
from ctypes import wintypes
import schedule, time
import apscheduler

cwd = os.getcwd()
bgdir = (cwd + r"\BackgroundChanger\Backgrounds")
backgrounds = [bg for bg in listdir(bgdir) if isfile(join(bgdir, bg))]
rand = random.SystemRandom()
img_path = (bgdir + "\\" + rand.choice(backgrounds))


def changebackground():
    SPI_SETDESKWALLPAPER  = 0x0014
    SPIF_UPDATEINIFILE    = 0x0001
    SPIF_SENDWININICHANGE = 0x0002

    user32 = ctypes.WinDLL('user32')
    SystemParametersInfo = user32.SystemParametersInfoW
    SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint
    SystemParametersInfo.restype = wintypes.BOOL
    print(SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, img_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE))

schedule.every(20).seconds.do(changebackground)


while 1:
    schedule.run_pending()
    time.sleep(1)
