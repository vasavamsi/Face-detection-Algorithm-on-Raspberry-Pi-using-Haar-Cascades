import numpy as np
import cv2 as cv
from rpi_config import *
from datetime import datetime as d
import webdav.client as wc
import os
import time

options = {
'webdav_hostname': "https://webdav.opendrive.com",
'webdav_login':    OPENDRIVE_USR, # replace with the needed username 
'webdav_password': OPENDRIVE_PWD # replce with the needed password
}
wcclient = wc.Client(options)

def haar_cascade(cnt):
     
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
#     cnt = 1
    path = "/home/pi/capture_test"
    path_2 = "/home/pi/send_photos"

    file_dir = os.listdir(path)
    file_dir.sort()
    
    if len(file_dir) > 5:   
        while (len(file_dir) != 0):
            file_dir = os.listdir(path)
            file_dir.sort()
            if len(file_dir) == 0:
                False
                break
            number = cnt
#             file_name=CAPTURE_FOLDER+"{}.jpg".format(date_string)
            file_name = CAPTURE_FOLDER+"{}.jpg".format(number)
            wcclient.upload_sync(remote_path=REMOTE_PATH_1+"{}".format(file_name[22:]), local_path=file_name)
            print("photo sent to my opendrive in the folder named 'Captured_images' ")
            img_1 = cv.imread(file_name)
            img = img_1
            img_1 = cv.cvtColor(img_1, cv.COLOR_BGR2RGB)
            gray_1 = cv.cvtColor(img_1, cv.COLOR_RGB2GRAY)  
            faces_1 = len(face_cascade.detectMultiScale(gray_1))
    
            if faces_1 > 0:
                cv.imwrite(os.path.join(path_2 , "%s.jpg") % str(number), img)
                print("the face has been detected and sent to my opendrive in the folder named 'Output_images'")
                wcclient.upload_sync(remote_path=REMOTE_PATH_2+"{}".format(file_name[22:]), local_path=file_name)
                print("Sent to cloud")
            del_path = os.path.join(path, file_name)
            os.remove(del_path)
            cnt += 1

            
    else:
        return
#         if cnt > len(file_dir):
#             break
    
    """
        elif (cnt%10 == 0):
            for n in range(cnt-9, cnt+1):
                number = n
                filename = CAPTURE_FOLDER+"{}.jpg".format(number)
                del_path = os.path.join(path, filename)
                os.remove(del_path)
            print("10 files have been deleted from the input directory")   
     """
        

cnt = 1
while True:
    n = haar_cascade(cnt)
    cnt = n
#     break
