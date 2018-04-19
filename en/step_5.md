## Time stamping the video

Each time the hamster runs in the wheel, a new video will be recorded. Because all the videos are named `vid.h264`, the files will constantly overwrite each other. This can be fixed by adding a time stamp to the video.

[[[generic-python-timestamps]]]

- Try and add a timestamp to the video file, so that the date, hour and minute is added to the filename.

--- hints --- --- hint ---
The timestamp codes are as follows
- Year = `%Y`
- Month = `%m`
- Day = `%d`
- Hour = `%H`
- Minute = `%M`
--- /hint --- --- hint ---
- To get the current date and time, you can use:
```python
now == datetime.now()
```
--- /hint --- --- hint ---
The full code, to be included in your `hamster_awake` function is as follows:
```python
def hamster_awake():
    now = datetime.now()
    camera.start_recording('/home/pi/hamster/{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}.h264'.format(now))
	camera.wait_recording(60)
    camera.stop_recording()
```
--- /hint --- --- /hints ---
