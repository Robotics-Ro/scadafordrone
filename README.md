# scadafordrone
SCADA for telloedu

SYSTEM

Jetson nano - tello EDU - Controller

### REFERENCE
**https://github.com/hanyazou/TelloPy**

### VIRTUAL ENVIRONMENT
```
$ python3 -m venv --system-site-packages .venv
```

#### SIMPLE TAKEOFF
```
$ python -m tellopy.examples.simple_takeoff
```

#### VIDEO EFFECT
```
$ python -m tellopy.examples.video_effect
```

#### KEYBOARD AND VIDEO
```
$ sudo apt install mplay
$ python -m tellopy.examples.keyboard_and_video
```

```
Controls:
- tab to lift off
- WASD to move the drone
- space/shift to ascend/descent slowly
- Q/E to yaw slowly
- arrow keys to ascend, descend, or yaw quickly
- backspace to land, or P to palm-land
- enter to take a picture
- R to start recording video, R again to stop recording
  (video and photos will be saved to a timestamped file in ~/Pictures/)
- Z to toggle camera zoom state
  (zoomed-in widescreen or high FOV 4:3)
```
