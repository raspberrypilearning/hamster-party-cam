## Taking multiple pictures

Try taking several pictures. Can you spot the problem with the way the code works?

--- collapse ---
---
title: Answer
---
If your hamster moves around more than once, a new picture is taken that overwrites the previous one, and you only end up with one picture.

--- /collapse ---

We would like to be able to save lots of different hamster pictures, so let's change the code to allow this.

- Add a variable called `pic` just below the lines of code where you `import` the libraries. The variable should start off being equal to 1.

[[[generic-python-creating-a-variable]]]

- Find the line in your code which takes the picture.
    ```python
    camera.capture('/home/pi/hamster/image.jpg')
    ```
- Concatenate the variable `pic` into the file name so that the number stored in `pic` is added to the end. Because `pic` is a number, we have to convert it to a string with `str()` to be able to join it with the file name. `pic` starts off as 1, so the first saved image will be `image1.jpg`.

    ```python
    camera.capture('/home/pi/hamster/image' + str(pic) + '.jpg')
    ```

- After the picture is taken, add 1 to the `pic` variable so that you get a different number next time.

- You will also need to type in `global pic` at the start of your function (immediately after `def hamster_awake(input)`). This allows you to update the variable `pic` from inside the function.

--- collapse ---
---
title: Solution
---

Here is the solution:
```python
pic = 1

def hamster_awake(input):
    global pic
    camera = PiCamera()
    camera.capture('/home/pi/hamster/image' + str(pic) + '.jpg')
    pic += 1
    sleep(0.2)
```
--- /collapse ---

- Save your work and then run the program again by pressing **F5**, while moving the hamster wheel. To end the program, press the **CTRL** and **C** keyboard buttons at the same time.

- Look in the `hamster` folder and check that multiple images have been saved.
