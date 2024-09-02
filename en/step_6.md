## Get the party started with lights

While your hamster is wide awake, you can use the LEDs to create a little disco for it.

- First, below where you have created all your LED objects, create a list containing all the LEDs.

```python
lights = [green, red, yellow, blue]
```

- Next, create a function called `disco`.

```python
def disco():
```

- Inside the `disco` function, you want to write some code that will randomly choose an LED and turn it on, then wait for a quarter of a second, and then turn a random light off. It should do this 240 times, so that the lights will be flashing for a minute.

--- hints --- --- hint ---
You can choose a LED to randomly turn on using the `choice` method you have imported.

```python
choice(lights).on()
```

And you can use the same method to turn off a random LED.

```python
choice(lights).off()
```
--- /hint --- --- hint ---
You can use a `for` loop to repeat this command as many times as you need.
```python
def disco():
	for i in range(240):
		choice(lights).on()
		sleep(0.25)
		choice(lights).off()
```		
--- /hint --- --- hint ---
Within the function, you'll want to turn all the lights off at the end of the minute.
```python
def disco():
	for i in range(240):
		choice(lights).on()
		sleep(0.25)
		choice(lights).off()
	for light in lights:
		light.off()
```		
--- /hint --- --- /hints ---

- Test your function by running your code and then typing `disco()` into the Python shell.

- Once your `disco` function causes your LEDs to randomly flash, you can go into your `hamster_awake` function and add a call of the `disco` function after the `record_video` command.

```python
def hamster_awake():
    now = datetime.now()
    camera.record_video('/home/pi/hamster/{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}.mp4'.format(now))
    disco()
```
