# Yolov8 Tutorial
This Jupyter Notebook will provide the basic tutorial on how to get started with yolov8 model. We will start by creating a development environment (conda or docker).

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


**Install pip**

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