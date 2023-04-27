import cv2
import numpy as np

# Capture a video frame.
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    # Capture the current frame.
    ret, frame = cap.read()

    # Convert the frame to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a blur to the grayscale image.
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Find the contours of the hand in the blurred image.
    contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour in the hand.
    largest_contour = max(contours, key=cv2.contourArea)

    # Extract the convex hull of the largest contour.
    hull = cv2.convexHull(largest_contour)

    # Find the fingertips of the hand.
    fingertips = []
    for i in range(len(hull) - 1):
        if hull[i][0][0] < hull[i + 1][0][0]:
            fingertips.append(hull[i])

    # Count the number of fingertips.
    num_fingers = len(fingertips)

    # Display the number of fingers on the screen.
    cv2.putText(frame, str(num_fingers), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # Display the frame.
    cv2.imshow("Frame", frame)

    # Check if the user wants to quit.
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the capture.
cap.release()

# Close all windows.
cv2.destroyAllWindows()