# Software installation

You'll need to make sure you have the following packages installed to proceed with the workshop.

You'll need to be online to install packages.

First update and upgrade your system. Enter the following commands in to the terminal:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Now install the packages you'll need:

```bash
sudo apt-get install python3-picamera python3-pip
```

You'll also need to install the Pibrella library from pip:

```bash
sudo pip-3.2 install pibrella
```

Test you have everything you need by entering the following command:

```python
sudo python3 -c "import picamera, pibrella"
```

This should show the following:

```
Pibrella exiting cleanly, please wait...
Stopping flashy things...
Stopping user tasks...
Cleaning up...
Goodbye!
```

If you get an error saying `No module named` then check you entered the commands above correctly.
