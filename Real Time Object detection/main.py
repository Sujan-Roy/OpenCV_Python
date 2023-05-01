import cv2
import yolo

# Load the YOLOv7 model.
model= ff

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    boxes, confidences, classes = yolo.detect_objects(model, frame)

 
    for box, confidence, class_id in zip(boxes, confidences, classes):
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, str(class_id), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))

    
    cv2.imshow("Object Detection", frame)

   
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()