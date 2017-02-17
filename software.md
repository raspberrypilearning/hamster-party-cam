# Software installation

You'll need to make sure you have the following packages installed to proceed with your hamster party cam.

You'll need to be online to install packages.

1. First, update and upgrade your system. You can do this by opening a **terminal window** by clicking on the terminal icon:

  ![Terminal](images/terminal.png)

1. Now type the following commands to ensure you are up to date:

  ```bash
  sudo apt-get update
  sudo apt-get upgrade
  ```

1. Now install the packages you'll need:

  ```bash
  sudo apt-get install python3-picamera python3-pip
  ```

1. You'll also need to install the Explorer HAT library:

  ```bash
  sudo apt-get install python3-explorerhat
  ```

1. Check you have the Explorer HAT installed correctly by running the following command:

  ```bash
  sudo python3 -c "import picamera, explorerhat"
  ```
  This should show the following:

  ```python
  Explorer HAT Pro detected...
  ```

  If you get an error saying `No module named` then check you entered the commands above correctly.
