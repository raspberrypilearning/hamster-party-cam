from gpiozero import LED, Button
from random import choice
from picamera import PiCamera
from datetime import datetime
from time import sleep
import pygame

pygame.init()
my_sound = pygame.mixer.Sound('/home/pi/hamster/Never.wav')

camera = PiCamera()
green = LED(17)
red = LED(22)
yellow = LED(9)
blue = LED(11)
wheel = Button(10)
lights = [green, red, yellow, blue]


def hamster_awake():
    now = datetime.now()
    camera.start_recording('/home/pi/hamster/{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}.h264'.format(now))
    disco()
    camera.stop_recording()
        

def disco():
    my_sound.play()
    for i in range(60):
        choice(lights).on()
        sleep(0.25)
        choice(lights).off()
    for light in lights:
        light.off()
    my_sound.stop()



wheel.when_pressed = hamster_awake

