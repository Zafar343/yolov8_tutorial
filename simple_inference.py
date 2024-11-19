import os
import glob
import tqdm
from ultralytics import YOLO
import cv2
# from sklearn.metrics import classification_report, confusion_matrix

# initialize the pretrained coco model
model = YOLO('yolov8n.pt')      # for custom model just replace 'yolov8n.pt' with your model path
# Display model information (optional)
model.info()

# define the image path
img_path = '/home/zafar/yolov8_tutorial/images/test_1.png'

image = cv2.imread(img_path)

# Display the image first, it will also test the Display inside docker container
cv2.imshow('Test image', image)
cv2.waitKey()
cv2.destroyAllWindows()

# perform inference
results = model(image, verbose=False)
# preds   = model.predict(image, conf=0.2, save_txt=True, save_conf=True)

# # Assuming `true_labels` is a list of your true labels for the test set
# predicted_labels = [pred[0].pred.argmax(-1).cpu().numpy() for pred in predictions]  # Get most likely class

# # Now use sklearn to get the classification report and confusion matrix
# print(classification_report(true_labels, predicted_labels))
# print(confusion_matrix(true_labels, predicted_labels))

# To get the prediction results from the yolo output
# results[0].boxes
# Vehicle ids in coco: 3, 4, 6, 7, 8 (4 is motorcycle)
# Person id in coco: 1
# Bicycle id in coco: 2

# get the annotated image after yolo inference
annotated_frame = results[0].plot()

cv2.imshow('Preds', annotated_frame)
cv2.waitKey()
cv2.destroyAllWindows()

# custom annotation by filtering out some preds based on conf and cls ids
for result in results[0].boxes:
    class_id   = result.cls.cpu().numpy()
    confidence = result.conf.cpu().numpy()
    bbox       = result.xyxy[0].cpu().numpy()  # Get the bounding box as [x1, y1, x2, y2]
    # filter out the unnecessary classes based on class ids provided above
    print(f"Class: {class_id[0]}, Confidence: {confidence[0]}, BBox: {bbox}")


vid_path = '/home/zafar/Desktop/30m_up_to_down.MOV'

# Open the input video
cap = cv2.VideoCapture(vid_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.2)
    annotated_frame = results[0].plot()
    cv2.imshow('Video Inference', annotated_frame)
    cv2.waitKey(10)
cv2.destroyAllWindows()
cap.release()    

print()