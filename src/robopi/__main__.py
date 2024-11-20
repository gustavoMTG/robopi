import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error, could not open camera")
    exit()

print("Camera opened!")