## Get the party started with lights

We can add extra fun to the Python program by making it use features of the Explorer HAT. For example, why not make the lights come on in disco mode when a hamster triggers the switch?

- Have the `hamster_party.py` file open in the Python 3 (IDLE) editor.

- Add a new line of code below the `import` statements:

	```python
	import random
	```

- Below the line `pic = 1`, add a list of the LED lights on the Explorer HAT like this:

	```python
	colours = [explorerhat.light.red, explorerhat.light.yellow, explorerhat.light.green, explorerhat.light.blue]
	```
- Below the list, create a disco function that will do the following:

    * Choose a random light from the list
    * Switch it on for 0.2 seconds
    * Switch it off

    This sequence should be repeated 25 times so the hamsters see 25 different randomly chosen lights.

[[[generic-python-simple-functions]]]

[[[generic-python-random-choice]]]

--- hints ---
--- hint ---
Here is some pseudo code for the function you are trying to write:
```python
FUNCTION disco()
    FOR i FROM 1 TO 25
        SET result = RANDOM(colours)
        TURN result ON
        WAIT 0.2 SECONDS
        TURN result OFF
END FUNCTION
```
--- /hint ---

--- hint ---
Here is the solution:
```python
def disco():
    for i in range(25):
        result = random.choice(colours)
        result.on()
        sleep(0.2)
        result.off()
 ```
--- /hint ---
--- /hints ---

- Find the line of code that takes the picture and add `disco()` below it to call your disco function.

- Save and test your code. Your hamster wheel switch should now trigger some disco lights on the Explorer HAT. The hamsters will love that!
