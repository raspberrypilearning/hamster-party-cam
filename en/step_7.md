## Hamsters need music to dance

Finally, let's trigger some tunes for the hamsters to dance to by downloading a sound file you like. It will need to be a `.wav` file.

You can play sound files using the Python `pygame` module.

[[[generic-python-playing-sound-files]]]

- Beneath where you created your LED objects, initialise pyagme and load up the sound file you want to play.

```python
pygame.init()
my_sound = pygame.mixer.Sound('path/to/my/soundfile.wav')
```

- At the start of the disco function, you waant the sound file to start playing. At the end of the function, once all the lights have stopped flashing, you can stop the sound file.

--- hints --- --- hint ---
Replace the comments in this code with your lines to start and stop playing the sound file.
```python
def disco():
	# Add a line here to start playing the sound
    for i in range(60):
        choice(lights).on()
        sleep(0.25)
        choice(lights).off()
    for light in lights:
        light.off()
	# Add a line here to stop playing the sound
```
--- /hint --- --- hint ---
Here's the completed function
```python
def disco():
    my_sound.play()
    for i in range(60):
        choice(lights).on()
        sleep(0.25)
        choice(lights).off()
    for light in lights:
        light.off()
    my_sound.stop()
```
--- /hint --- --- /hints ---
