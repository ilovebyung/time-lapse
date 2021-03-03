from time import sleep
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1920,1080)
    for filename in camera.capture_continuous('/home/pi/Pictures/{timestamp:%y%m%H%M%S}.jpg'):
        sleep(60)
