# Yolov8 Tutorial
For getting started with yolov8 inference, training and validation We will first create a development environment (conda or docker).

### Making a conda environment
I assume anaconda already installed if not head over to anconda website and follow the instructions to install the anaconda.

anaconda website: [Link text](https://docs.anaconda.com/anaconda/install/)

To create conda environment follow the following steps:

Open up Anaconda Prompt on windows, on linux and macOS open up terminal and run following commands one by one

```conda create -n yolo_tutorial python=3.10```

```conda activate yolo_tutorial```

After creating and activating conda environment install pip (package manager) to install the required dependencies

```conda install pip```

Please note that while installing the dependency packages in the active conda environment always use ```python3 -m pip install Package``` otherwise the dependencies can end up being installed in some global python environment.

Install the Ultralytics yolo package for getting started with yolov8
```python3 -m pip install ultralytics```

### Making and using Docker environment
For this tutorial I will be using a docker environment. Only thing needed for this is the Docker should be installed in your PC. If not follow the the Docker official installation guide for your OS.

Windows: [Link text](https://docs.docker.com/desktop/setup/install/windows-install/)

Linux: [Link text](https://docs.docker.com/engine/install/ubuntu/)

MacOS: [Link text](https://docs.docker.com/desktop/setup/install/mac-install/)

Once the Docker installation is done follow along to pull a docker image and start the docker container.

**Pulling a docker image from Dockerhub**

```docker pull zafar343/dispimgcu11.8:latest```

Check the image locally ```docker images```

**Starting docker Container**

```docker run -it -d -v $PWD:$PWD -w $PWD --gpus all -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -name yologui_container zafar343/dispimgcu11.8```

Before running container check your display parameters if you are using linux ```echo $DISPLAY```

Once docker container is started head over to vscode and attach the container in current window. Check display parameters again inside the container and verify the display if parameters match ```xeyes```

If get authorization issue then add docker in the authorized list for the xhost ```xhost +local:docker```


**Install pip inside docker container**

```apt-get update```

```apt-get install python3-pip -y```

```pip --version```

Install ultralytics package: ```pip install ultralytics```

Check the installed packages: ```pip list```

Now you are good to go, we will test the Display first and then move on

## Datasets

BDD dataset (3 class only) for inference, evaluation and training. Download the BDD dataset from here: [Link text]()

Open youtube videos and images for inference and visualization only

For inference we can use any images or videos but for training and evaluating a yolo model the dataset should be in the following format

    BDD_dataset/
    ├── train
    │   ├── b1c66a42-6f7d68ca.jpg
    │   ├── b1c66a42-6f7d68ca.txt
    │               ...
    │   ├── b1d9e136-9ab25cb3.jpg
    │   └── b1d9e136-9ab25cb3.txt
    └── val
        ├── b1c66a42-6f7d68ca.jpg
        ├── b1c66a42-6f7d68ca.txt
                    ...
        ├── b1ceb32e-813f84b2.jpg
        └── b1ceb32e-813f84b2.txt

Yolo alogorithms assume the annotations in a .txt file. The annotation format inside an annotation file should be like:```c x_center y_center w h```. where `c` is the object class, `x_center` and `y_center` are box center point while `w` and `h` are box height and box width respectively. The box coordinates should also be normalized with height and width of image. Image and the label files should be in the same directory.

Dataset can be downloaded from here (3 class BDD dataset): [Link text](https://drive.google.com/drive/folders/1DXNAiwh9OKfuP6fPPZe-YNEazCekwuZi?usp=sharing)

**How to prepare the data for training and inference?**

Ultralytics package now provides an option to use the directory paths in the data config file for training and validation. Only thing is to make sure the images and labels are avialable in the same path. ALternatively use following linux commands to make the `train.txt` and `val.txt` first:

**For `train.txt`:** ```find full/path/to/train/folder | grep .jpg > path/to save/location/train.txt```

**For `val.txt`:** ```find full/path/to/val/folder | grep .jpg > path/to save/location/val.txt```

Make sure to provide the full path to `find` otherwise the YOLO will trough Path errors. Also, make sure to keep the label files in the same folder. Now update the `data.yaml` with the paths of your `train.txt` and `val.txt`. The `train.txt` or `val.txt` look like following:

```
1 /home/zafar/old_pc/data_sets/BDD_dataset/Bdd_uncleaned/3class_bdd/val/b2bee3e1-80c787bd.jpg
2 /home/zafar/old_pc/data_sets/BDD_dataset/Bdd_uncleaned/3class_bdd/val/b6663f36-805c1a0e.jpg
3 /home/zafar/old_pc/data_sets/BDD_dataset/Bdd_uncleaned/3class_bdd/val/b248306f-a5089e94.jpg
4 /home/zafar/old_pc/data_sets/BDD_dataset/Bdd_uncleaned/3class_bdd/val/b7ad967b-5ffacb53.jpg
5 /home/zafar/old_pc/data_sets/BDD_dataset/Bdd_uncleaned/3class_bdd/val/b9fb5382-990e8173.jpg
```

To choose a subset of your full training or validation data you can use `sed` or `shuf` with appropriate options to make `train.txt` and `val.txt` files containing only the subset of original data.

## Training on custom data

Preapare the data for training and validation by following the above guide. Once every thing is ready run the following command.

```python3 train.py --model yolov8n.pt```

Use `--cfg` and give a config file (`yolov8n.yaml`) instead, if you are trying to train from scratch.

For validation run:  ```python3 val.py --model yolov8n.pt```

For running object tracking: ```pyhton3 track.py --model yolov8n.pt --source 0```

use the path of video instead of `0` if doing tracking on a video
