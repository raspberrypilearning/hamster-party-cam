import pibrella, picamera, time, random, os

colours = [pibrella.light.red,
           pibrella.light.amber,
           pibrella.light.green]

def disco():
    for i in range(25):
        result = random.choice(colours)
        result.on()
        time.sleep(0.2)
        result.off()

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    pic = 1
    while True:
        if pibrella.input.a.read():
            camera.capture('/home/pi/hamster/image%03d.jpg' % pic)
            print("Party!")
            os.system('omxplayer hamsterdance.mp3 &')
            disco()
            time.sleep(10)
            pic += 1
        time.sleep(0.01)    
