## Take pictures of the hamsters

- Create a folder called `hamster` for your hamster party pictures.

[[[rpi-gui-creating-directories]]]

- Open **Python 3 (IDLE)**

[[[rpi-gui-idle-opening]]]

- Create a blank file and save it with the name `hamster_party.py` in the `hamster` directory you just created.

- Begin your code by importing the `explorerhat` library, the `picamera` library, and the `sleep` function from the `time` library:

    ```python
	import explorerhat
	import picamera
	from time import sleep
    ```

- Add a function called `hamster_awake(input)` which contains code to take a picture of the hamster and then wait 0.2 seconds.

	```python
	def hamster_awake(input):
		# Fill in the code here to take a picture

	```

[[[rpi-picamera-take-photo]]]

--- hints ---
--- hint ---
Read the information on **Taking a photograph with PiCamera** to work out how to initialise a camera object, and how to capture a photograph. Make sure you save your photograph in the `hamster` directory you created earlier.
--- /hint ---

--- hint ---
Here is some pseudo code for what you need to do:

```
FUNCTION hamster_awake(input)
    SET camera = PICAMERA OBJECT
    TAKE PICTURE AND SAVE AS /home/pi/hamster/image.jpg
    WAIT 0.2 SECONDS
END FUNCTION
```

--- /hint ---

--- hint ---
Here is a solution:

```python
camera = PiCamera()
camera.capture('/home/pi/hamster/image.jpg')
sleep(0.2)
```
--- /hint ---

--- /hints ---


- Below the function you just wrote, add some code to call this function when the reed switch is triggered. Make sure that this code is **not** indented.

    ```python
    explorerhat.input.one.changed(hamster_awake)
    ```

- Save your code and run it by pressing **F5**. Check that when you turn the wheel, a picture is taken and saved in the `hamster` directory.
