# Potty Road  
Realtime pothole severity classifier powered by Deep Learning  

## Installation Instructions
Though one can work with the project without an virtual environment,  it is recommended to use one so 
as to avoid conflicts with other projects.

0. Make sure that you have `Python 3`, `python-3-devel`, `gcc`, `virtualenv`, and `pip` installed.     
1. Clone the repository

    ```bash
        $ git clone https://github.com/sanjay-thiyagarajan/PottyRoad.git
        $ cd PottyRoad
    ```  
2. Create a python 3 virtualenv, activate the environment and Install the project dependencies.   

    a. Linux Users:
  
    ```bash  
        $ virtualenv vir
        $ source vir/bin/activate
        $ pip3 install -r requirements.txt 
    ```  

    b. Windows Users:  

    ```bash
        $ virtualenv vir
        $ vir\Scripts\Activate
        $ pip3 install -r requirements.txt
    ```   

You have now successfully set up the project on your environment.  

## Tech Stack  
1) TensorFlow
2) Python
3) OpenCV
4) Tkinter  

## Usage  
a) Command line mode:  
```
  python3 classifier.py --inputvideo="path/to/video.mp4"
```
b) Simple GUI:  
```
  python3 GUI.py
```  

## Screenshots  
![Pothole Classification_screenshot_10 01 202344](https://user-images.githubusercontent.com/42594454/211483614-1f81a77e-a1f6-430a-8220-49f3e743b7be.png)
![Pothole Classification_screenshot_10 01 202333](https://user-images.githubusercontent.com/42594454/211483656-4702cc6f-806c-4c40-b87d-6176982a97f1.png)
![Pothole Classification_screenshot_10 01 2023](https://user-images.githubusercontent.com/42594454/211483680-8553fcaf-d84a-46e8-8d17-70ffe7ff4b05.png)
![Pothole Classification_screenshot_10 01 20233](https://user-images.githubusercontent.com/42594454/211483699-728bc7f4-2e44-4e05-92a1-807931b5f128.png)
![Pothole Classification_screenshot_10 01 2023444](https://user-images.githubusercontent.com/42594454/211484487-4a99f3b7-f6e3-44d0-9013-62f2d7b7b461.png)
