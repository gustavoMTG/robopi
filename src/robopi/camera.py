"""
robopi.camera
~~~~~~~~~~~~~

This module contains the camera support. Initially we are providing support
for the Raspberry Pi Camera Rev 1.3. In the future this module should contain 
also support for other cameras. This way we abstract the main program of the 
mechanism by which the image array is provided
"""

import sys
# For reaching system level dependencies when isolated in virtual environment
# such as picamera2
sys.path.append("/usr/lib/python3/dist-packages")

import numpy as np
from picamera2 import Picamera2, Preview


picam2 = Picamera2()

camera_config = picam2.create_preview_configuration({"format": "RGB888"})
picam2.configure(camera_config)
picam2.start_preview(Preview.NULL)

picam2.start()

def get_array() -> np.ndarray:
    """
    Function for supporting Raspberry Pi Camera Rev 1.3.

    return: numpy.ndarray
    """
    return  picam2.capture_array() # returns numpy array