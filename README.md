# Smile_Detector
 This computer vision model uses OpenCv Haar-cascadec classifiers to detect fronal face and within the region of face, looks for eyes and ssmile. The program uses laptop's webcam to access live video, extracts its frame, detects the features and draws rectangle surrounding the feature and combines back the frames to output video in real time.
 
 ## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### System Prerequisites

you need to install

```
Anaconda
Python 3.6
OpenCV
```

### Installing

```
Anaconda :
https://docs.anaconda.com/anaconda/install/

Python 3.6 :
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html

OpenCV:
https://pypi.org/project/opencv-python/
```
 
 ## Running the application:
 
 
 **Non-smiling face** <br />
 <img width="350" height="500" alt="Screen Shot 2020-01-02 at 9 51 48 AM" src="https://user-images.githubusercontent.com/41305591/71673021-95f3d600-2d45-11ea-8ed7-770b606c043d.png"> <br />
 
 **Smiling face** <br />
 <img width="350" height="500 " alt="Screen Shot 2020-01-02 at 9 57 06 AM" src="https://user-images.githubusercontent.com/41305591/71673262-57125000-2d46-11ea-9fde-6f3c6b275429.png"> <br />
 
 OpenCV is not the best way for detecting features accurately. In the second picture, you could notice that my right eye was not detected by this model. This model gives a couple of positive false which could be tuned by tuning the model a bit. I am looking forward to make improvements to this model and implement other models like FaceNet for facial recognition.
 
 **Acknowledgements** <br />
 * Udemy
 * Hadelin de Ponteves
 * Kirill Eremenko
 
 
 
