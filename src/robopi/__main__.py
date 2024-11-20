import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error, could not open camera")
    exit()

print("Camera opened!")

ret, frame = cap.read()
if ret:
    cv2.imwrite("captured_frame.jpg", frame)
    print("Image saved")
else:
    print("Error capturing the frame")

cap.release()