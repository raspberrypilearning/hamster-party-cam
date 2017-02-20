import explorerhat
import picamera
from time import sleep
import random

pic = 1
colours = [explorerhat.light.red, explorerhat.light.yellow, explorerhat.light.green, explorerhat.light.blue]

def disco():
    for i in range(25):
        result = random.choice(colours)
        result.on()
        sleep(0.2)
        result.off()

def hamster_awake(input):
    global pic
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.capture('/home/pi/hamster/image%03d.jpg' % pic)
        print("Party!")
        disco()
        pic += 1
        sleep(0.2)


explorerhat.input.one.changed(hamster_awake)
