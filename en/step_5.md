## Time-stamping the video

Each time the hamster runs in the wheel, a new video will be recorded. Because right now each video gets named `vid.h264`, every new file will overwrite the previous one. You can fix that by adding a time stamp.

[[[generic-python-timestamps]]]

- Try and add a time stamp to the video file, so that the date, hour, and minute is added to the file name.

--- hints --- --- hint ---
The time stamp codes are:
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
The full code to be included in your `hamster_awake` function is:
```python
def hamster_awake():
    now = datetime.now()
    camera.start_recording('/home/pi/hamster/{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}.h264'.format(now))
	camera.wait_recording(60)
    camera.stop_recording()
```
--- /hint --- --- /hints ---
