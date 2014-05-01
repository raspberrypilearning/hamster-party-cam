#Hamster Party Cam

###Introduction
Hamsters are nocturnal, which means that they sleep in the day time and come out at night. This means that when you are sleeping, your hamsters are up and about and when you are up and about, your hamsters are sleeping! 

Really we need to find some way of being able to see what the hamsters are up to during the night. I suspect they are partying. 

In this project, we are going to use a Raspberry Pi Camera and a Pibrella with a Raspberry Pi to take pictures and video of the hamsters, that is triggered by their movement. 

##Step 0: Setting up your Raspberry Pi, Pi Camera and Pibrella
You will need to set up your Raspberry Pi to take part in this activity. See the [Raspberry Pi Start Guide]() here to get you up and running.

You will also require a Raspberry Pi Camera Module connected to your Raspberry Pi. See the [Raspberry Pi Camera Guide](http://www.raspberrypi.org/help/camera-module-setup/) here to connect your pi camera to your Raspberry Pi. Then follow [Raspberry Pi Camera Setup Tutorial](https://github.com/raspberrypilearning/python-picamera-setup) to enable the camera, test it, and download the picamera library.

Next, you will need a Pibrella board attached to the GPIO pins on your Raspberry Pi. See the [Pibrealla](https://github.com/raspberrypilearning/pibrella-setup) guide here to learn how to add the board and download the pibrella library. 

Phew, that is a fair bit of setup, but it will be worth it in the end.

##Step 1: Create a Pressure Sensitive Switch
We only want the Raspberry Pi to take pictures of the hamsters when they are out and having a good time. (No doubt they are throwing out some robot dance moves in your absence.) So you will need to create a switch that triggers the camera to make a program run in order to take pictures of the party. 

###Activity Checklist:
1. Plug one end of a male to male jumper wire into the input socket on your Pibrella labelled 'A'.

	![](jumper-wire.png)
	
2. Next connect the other end of the jumper wire to a crocodile cable. 
	
	![](crocodile-cable.png)
	
3. Connect the other end of the crocodile cable to a rectangle of tin foil the size of a postcard (A5).

	![](tin-foil.png)

4. Place the tin foil in the hamster cage on the floor. When the hamster steps on the tin foil, it will trigger the camera to take a photo, so make sure you put it somewhere near the camera!

##Step 2: Create a Python Program to take Pictures of the Party
With a Pi Camera connected, and a pressure senstive switch attached to the Pibrella board, you can now write a program in Python to detect movement, and take a picture.

###Activity Checklist:
1. Open an LXTerminal window and type `mkdir hamster` and press **enter** to create a folder for your hamster party pictures.
2. Then type `sudo idle &` and press **enter** to load the Python environment IDLE.
2. Click on **File** and **New Window** to open a new text editor file.
3. Save the file by clicking on **File** and **Save As** and name the file `hamster` and click **Ok**.
4. Now type the following code into your hamster file:

	```python
	import pibrella, picamera, time

	with picamera.Picamera() as camera:
    	camera.resolution = (1024, 768)
    	pic = 1
    	while True:
        	if pibrella.input.a.read():
            	camera.capture('/home/pi/hamster/image%03d.jpg' % pic)
            	print("snap!")
            	pic += 1
        	time.sleep(0.2)    
	```            
5. Save your work by clicking on **File** and **Save**
6. To test that your program works, Click on **File** and **Run Module**. Then touch the tin foil a few times. To end the program press **CTRL** and **C** on the keyboard at the same time.
7. Look in the hamster folder or directory by navigating the Main Menu to **Accessories** and **File Manager** then double click the hamster folder icon.

##Community:
Based on an idea submitted for the Raspberry Pi Poster Competition December 2013 by..

![](poster.png)
