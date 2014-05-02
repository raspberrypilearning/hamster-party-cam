#Hamster Party Cam

###Introduction
*"Hamsters are nocturnal, which means that they sleep in the day time and come out at night. This means that when you are sleeping, your hamsters are up and about and when you are up and about, your hamsters are sleeping!" - Violet* 

Really we need to find some way of being able to see what the hamsters are up to during the night. I suspect they are partying. 

In this project, we are going to use a Raspberry Pi Camera and a Pibrella with a Raspberry Pi to take pictures and video of the hamsters, that is triggered by their movement. 

##Step 0: Setting up your Raspberry Pi, Pi Camera and Pibrella
You will need to set up your Raspberry Pi to take part in this activity. See the [Raspberry Pi Start Guide](http://www.raspberrypi.org/help/quick-start-guide/) here to get you up and running.

You will also require a Raspberry Pi Camera Module connected to your Raspberry Pi. See the [Raspberry Pi Camera Guide](http://www.raspberrypi.org/help/camera-module-setup/) here to connect your pi camera to your Raspberry Pi. Then follow [Raspberry Pi Camera Setup Tutorial](https://github.com/raspberrypilearning/python-picamera-setup) to enable the camera, test it, and download the picamera library.

Next, you will need a Pibrella board attached to the GPIO pins on your Raspberry Pi. See the [Pibrealla](https://github.com/raspberrypilearning/pibrella-setup) guide here to learn how to add the board and download the pibrella library. 

Phew, that is a fair bit of setup, but it will be worth it in the end.

##Step 1: Create a Pressure Sensitive Switch
We only want the Raspberry Pi to take pictures of the hamsters when they are out and having a good time. (No doubt they are throwing out some robot dance moves in your absence.) So you will need to create a switch that triggers the camera to make a program run in order to take pictures of the party. 

###Activity Checklist:
1. Plug one end of a male to male jumper wire into the input socket on your Pibrella labelled 'A'.

	![](jumper-wire.JPG)
	
2. Next connect the other end of the jumper wire to a crocodile cable. 
	
	![](crocodile-cable.png)
	
3. Connect the other end of the crocodile cable to a rectangle of tin foil the size of a postcard (A5).

	![](tin-foil.png)

4. Place the tin foil in the hamster cage on the floor. When the hamster steps on the tin foil, it will trigger the camera to take a photo, so make sure you put it somewhere near the camera!

##Step 2: Create a Python Program to take Pictures of the Hamsters
With a Pi Camera connected, and a pressure senstive switch attached to the Pibrella board, you can now write a program in Python to detect movement, and take a picture.

###Activity Checklist:
1. Open an LXTerminal window and type `mkdir hamster` and press **enter** to create a folder for your hamster party pictures.
2. Then type `sudo idle &` and press **enter** to load the Python environment IDLE.
2. Click on **File** and **New Window** to open a new text editor file.
3. Save the file by clicking on **File** and **Save As** and name the file `hamster-party` and click **Ok**.
4. Now type the following code into your hamster file:

	```python
	import pibrella, picamera, time

	with picamera.Picamera() as camera:
    	camera.resolution = (1024, 768)
    	pic = 1
    	while True:
        	if pibrella.input.a.read():
            	camera.capture('/home/pi/hamster/image%03d.jpg' % pic)
            	print("Party!")
            	pic += 1
        	time.sleep(0.2)    
	```            
5. Save your work by clicking on **File** and **Save**
6. To test that your program works, Click on **File** and **Run Module**. Then touch the tin foil a few times. To end the program press **CTRL** and **C** on the keyboard at the same time.
7. Look in the hamster folder or directory by navigating the Main Menu to **Accessories** and **File Manager** then double click the hamster folder icon. You should see some image files.

##Step 3: Get the Party Started with Lights!
We can add extra fun to the Python program that uses more features of the Pibrella board. For example, why not trigger the lights to come on in disco mode when a hamster triggers the switch?

###Activity Checklist:
1. Make sure that `hamster-party.py` is open in a text editor still.
2. Add `random` to end of `import pibrella, picamera, time` in the first line.
3. Underneath make a space to add a list for the LED lights on Pibrella like this:
	
	```python
	colours = [pibrella.light.red, pibrella.light.amber, pibrella.light.green]
	``` 
4. Below the list create a disco function by typing the following:

	```python
	def disco():
	    for i in range(10):
	        result = random.choice(colours)
	        result.on()
	        time.sleep(0.2)
	        result.off()
	 ```
5. Then navigate to the line `print("Party!")` and add `disco()` underneath the line.

	![](hamster-code-2.png)
	
6. Save and test your code. Your pressure senstive switch should now trigger some disco lights on the pibrella. The hamsters will love that! 		        	

##Step 4: Hamsters need Music to Dance!
Finally let's trigger some tunes for the hamsters to dance to, by downloading a sound file like a `.mp3` or `.wav`and playing it using omxplayer. You can use your own sound files if you transfer them to your Raspberry Pi, just change the name of the file in the code. 

###Activity Checklist:
1. First you will need to put a a sound file onto your Raspberry Pi. You can do this either by connecting it to the internet and typing the following line into LXTerminal:
	
	`wget https:// `
	
	or, by transfering a sound file from a computer with a usb memory stick.
2. Add `sys, os` to the end of the `import` line.
3. Now navigate to the line `print("party!")` and underneath add `os.system('omxplayer hamsterdance.mp3 &')` *Note: that you will need to replace the name of the mp3 iwth the name of the file you are using if it is different from the one being used here.* 
3. Save the file and test that the program works by triggering the switch again.

###Final Project Code:
Your final project code should look something like this:

```python
import pibrella, picamera, time, random, os, sys

colours = [pibrella.light.red, pibrella.light.amber, pibrella.light.green]

def disco():
	for i  in range(10):
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
            pic += 1
        time.sleep(0.5)
```        

##Disclaimer:
Adding lights and music to the party is fun, but could keep *you* awake at night, and may become a little annoying to adults. It may also scare hamsters of a shy disposition. 

##Community:
Based on an idea submitted for the Raspberry Pi Poster Competition December 2013 by Violet.
It's been a pleasure to make this Raspberry Pi poster project idea a reality. 

![](poster.JPG)

##Licence:
Unless otherwise specified, everything in this repository is covered by the following licence:

![Creative Commons License](http://i.creativecommons.org/l/by-sa/4.0/88x31.png)

***Hamster Party Cam*** by the [Raspberry Pi Foundation](http://raspberrypi.org) is licenced under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

Based on a work at https://github.com/raspberrypilearning/hamster-party-cam
