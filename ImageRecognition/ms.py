import mss

with mss.mss() as sct:
    sct.shot(output='screenshot.png')