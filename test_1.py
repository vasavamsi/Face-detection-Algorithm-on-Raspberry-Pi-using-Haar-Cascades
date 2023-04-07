from picamera import PiCamera
from rpi_config import *
from datetime import datetime as d
import os

def capture():
    
    global counter1,queue,nine
    cnt = 1
    while(cnt > 0):
        number = cnt
        #date_string = d.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
#         file_name=CAPTURE_FOLDER+"{}.jpg".format(str(number).zfill(4))
        file_name=CAPTURE_FOLDER+"{}.jpg".format(number)
        camera.capture(file_name)
        #wcclient.upload_sync(remote_path=REMOTE_PATH_1+"{}".format(file_name[22:]), local_path=file_name)
        cnt += 1
        print ("Captured: ",file_name)
        if cnt > 1000:
            break 

camera = PiCamera()
while True:
    capture()
    break

# Code to be implemented as time stamp:

"""
while True:
    hour = int(d.now().strftime("%H"))
    minute = int(d.now().strftime("%M"))
    if (hour > 15) and (minute < 45):
        capture()
    else:
        print("sleeping........")
"""