import sys
# For reaching system level dependencies when isolated in virtual environment
# such as picamera2
sys.path.append("/usr/lib/python3/dist-packages")

from picamera2 import Picamera2, Preview


picam2 = Picamera2()

camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.NULL)

picam2.start()
im = picam2.capture_array() # returns numpy array