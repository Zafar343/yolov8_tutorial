from ultralytics import YOLO
import argparse
import torch

def train_yolov8():
    args   = parseArgs()
    # choose between training from scratch and training using a checkpoint
    device = torch.device(f"cuda:{args.device}" if torch.cuda.is_available() else "cpu")
    if args.config:
        model_type = args.config
    else:
        model_type = args.model
    # Load YOLO model    
    model = YOLO(model_type)

    # Train model
    model.train(
        # cfg =args.config,
        data        = args.data,
        epochs      = args.epochs,           
        batch       = args.batch_size,         
        imgsz       = args.img_size,          
        lr0         = args.initial_lr,                  
        project     = args.project,         
        name        = args.name,        
        device      = device,
        save_period = -1        
    )

def parseArgs():
    parser = argparse.ArgumentParser(description='AIADAS')
    parser.add_argument("--config", type=str, default=None,
                        help='provide a model config filename (.yaml) if training from scratch')
    parser.add_argument("--model", type=str, default='',
                        help='provide a model path (model.pt) if initializing from a pretrained checkpoint')
    parser.add_argument("--data", type=str, default='data.yaml', help='provide data.yaml path')
    parser.add_argument("--epochs", type=int, default=100, help='specify the number of epochs')
    parser.add_argument("--batch_size", type=int, default=16, help='specify the batch size')
    parser.add_argument("--img_size", type=int, default=640, help='specify the image size')
    parser.add_argument("--project", type=str, default='runs/Yolov8_Tutorial', help='name your project')
    parser.add_argument("--name", type=str, default='custom_training')
    parser.add_argument("--device", type=int, default=0, help='Chosse a gpu device')
    parser.add_argument("--initial_lr", type=float, default=0.01)

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    # Run training
    train_yolov8()