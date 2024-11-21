import numpy as np


def arraytransform(frame: np.ndarray) -> np.ndarray:
    height, width, channels = frame.shape

    frame[:, 20] = [255, 0, 0]
    frame[:, -20] = [0, 255, 0]
    frame[20, :] = [0, 0, 255]

    return frame