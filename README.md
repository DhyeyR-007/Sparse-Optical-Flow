# Sparse-Optical-Flow

Optical flow is a task of per-pixel motion estimation between two consecutive frames in one video. Basically, the Optical Flow task implies the calculation of the shift vector for pixel as an object displacement difference between two neighboring images. The main idea of Optical Flow is to estimate the object’s displacement vector caused by it’s motion or camera movements.

Sparse Optical Flow: 
It computes the motion vector for the specific set of objects (for example – detected corners on image). Hence, it requires some preprocessing to extract features from the image, which will be the basement for the Optical Flow calculation.
To solve the problem of sparse optical flow we have employed Lucas-Kanade algorithm:

Lucas-Kanade algorithm
The Lucas-Kanade method is commonly used to calculate the Optical Flow for a sparse feature set. The main idea of this method based on a local motion constancy assumption, where nearby pixels have the same displacement direction. This assumption helps to get the approximated solution for the equation with two variables.

Theory
Let’s assume that the neighboring pixels have the same motion vector (\Delta x, \Delta y). We can take a fixed-size window to create a system of equations. Let p_i = (x_i, y_i) be the pixel coordinates in the chosen window of n elements . Hence, we can define the equation system as:


Optical Flow applications:
Optical Flow can be used in many areas where the object’s motion information is crucial. Optical Flow is commonly found in video editors for compression, stabilization, slow-motion, etc. Also, Optical Flow finds its application in Action Recognition tasks and real-time tracking systems.
