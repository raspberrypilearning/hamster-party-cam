## Recording video of the hamster

- With your Raspberry Pi connected to a keyboard, monitor, and mouse, create a folder called `hamster` for your hamster party pictures.

[[[rpi-gui-creating-directories]]]

- Open **Python 3 (IDLE)**.

[[[rpi-gui-idle-opening]]]

- Create a blank file and save it with the name `hamster_party.py` in the `hamster` directory you just created.

- Begin your program by importing all the modules you will need for this project:

```python
from gpiozero import LED, Button
from random import choice
from picamera import PiCamera
from datetime import datetime
from time import sleep
import pygame
```

- Next you want to set up your LED, camera, and button objects. You can substitue your own pin numbers and LED colours for how you have set up your hardware.

```python
camera = PiCamera()
wheel = Button(10)
red = LED(17)
blue = LED(22)
green = LED(9)
yellow = LED(11)
```

- Add a function called `hamster_awake()` that contains code to take a 60-second video of the hamster.

```python
def hamster_awake(input):
	# Fill in the code here to record a video

```
[[[rpi-camera-record-video]]]

--- hints ---
--- hint ---
Read the information in 'Recording a video with a Raspberry Pi and Camera Module' to work out how to initialise a camera object and capture a video. Make sure you save your file in the `hamster` directory you created earlier.
--- /hint ---

--- hint ---
Here is some pseudo-code for what you need to do:

```
FUNCTION hamster_awake(input)
    START RECORDING A VIDEO AND SAVE AS /home/pi/hamster/vid.h264
    WAIT 60 SECONDS
	STOP RECORDING
END FUNCTION
```

--- /hint ---

--- hint ---
Here is a solution:

```python
camera.start_recording('/home/pi/hamster/vid.h264')
camera.wait_recording(60)
camera.stop_recording
```
--- /hint ---

--- /hints ---


- Below the function you just wrote, add some code to call this function when the reed switch is triggered. Make sure that this code is **not** indented.

```python
wheel.when_pressed = hamster_awake
```

- Save your code and run it by pressing <kbd>F5</kbd>. Check that when you turn the wheel, a video is recorded and saved in the `hamster` directory.

[[[rpi-bash-play-with-omxplayer]]]
