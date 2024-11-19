from ultralytics import YOLO
import argparse
import torch
import cv2

def track():
    args   = parseArgs()
    # choose between training from scratch and training using a checkpoint
    device = torch.device(f"cuda:{args.device}" if torch.cuda.is_available() else "cpu")
    # Load YOLO model    
    model = YOLO(args.model)

    cap = cv2.VideoCapture(args.source)

    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()
        # TODO: resize to less resolution to make computationally efficient

        if success:
            trackerRslts = model.track(frame, conf=args.conf, device=device, persist=True)    

            # Visualize the results on the frame
            annotated_frame = trackerRslts[0].plot()
            
            # Tips for project
            # get the predictions and extract the track id
            # make history buffer to store the predictions based on their Ids: {id: [[x y x y c cnf],[],[],[],[]]}
            # For direction simply take the difference of current box with box 5 frames ago and check if difference
            # is positive or negative to specify the appropriate direction
            # for left right use x coordinates of box and for forward/backward use y coordinates
            # for speed estimation clculate the euclidean distance usinf box coordinates: d = sqrt((x_2-x_1)^2 + (y_2-y_1)^2)
            # use following formula to calculate the speed of object s = (d/t)*(1/h), d comes from above it is distance
            # t is time can be obtained from video frame rate and h is box height, you can also use box width as well for vehicles

            # estimate the speed and direction
            # Display the annotated frame
            cv2.imshow("YOLO11 Tracking", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break
    cap.release()
    cv2.destroyAllWindows()


def parseArgs():
    parser = argparse.ArgumentParser(description='Yolo Tutorial')
    parser.add_argument("--model", type=str, default='/home/zafar/yolov8_tutorial/yolov8n.pt',
                        help='provide a model path (model.pt) if initializing from a pretrained checkpoint')
    parser.add_argument("--source", type=str, default='/home/zafar/Desktop/30m_up_to_down.MOV', help='provide video path if source is video else give the cmera ID')
    parser.add_argument("--device", type=int, default=0, help='Chosse a gpu device')
    parser.add_argument("--conf", type=float, default=0.25, help='Choose a confidence threshold')
    parser.add_argument("--tracker", type=str, default='bytetrack', help='Choose a tracker type')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    # Run training
    track()