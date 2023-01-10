# Potty Road  
A pothole severity classifier powered by Deep Learning  

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

## Usage  
a) Command line mode:  
```
  python3 classifier.py --inputvideo="path/to/video.mp4"
```
b) Simple GUI:  
```
  python3 GUI.py
```  
