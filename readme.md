MEDICAL ANALYSIS SYSTEM


1. Control and modify file : configuration.json
2. Run Start.py
3. Click Analysis button 
4  Control Python Console for the Result

--------------

DETAILS

CONFIGURATION FILE

Inside the configuration file you can specify all the functions you want to add to the system.
It starts with the definition of the tool to use: AWS Rekognition, YOLO, etc. And then you specify which module you want to load (specify the services that the system offers). In this case it was set up as an AWS Rekognition tool, and a patient status monitoring as an action.


STREAM VIDEO

Within two python scripts called EmotionAnalysis.py and MovementAnalysis.py, the function that allows images to be taken from video recording systems is specified.
The function concerned is part of the OpenCV library and is called: videoCapture (param).
In the case of the module implemented in this system, the function parameter is 0. This means that the images are taken directly from your local webcam. To be able to take advantage of an online video streaming stream, simply connect the device you intend to use in live streaming, and then add the URL of the device's direct streaming to the videoCapture () function parameter.

Official Documentation : https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html

-----------
