# Sparse-Optical-Flow

Optical flow is a task of per-pixel motion estimation between two consecutive frames in one video. Basically, the Optical Flow task implies the calculation of the shift vector for pixel as an object displacement difference between two neighboring images. The main idea of Optical Flow is to estimate the object’s displacement vector caused by it’s motion or camera movements.

Sparse Optical Flow: 

It computes the motion vector for the specific set of objects (for example – detected corners on image). Hence, it requires some preprocessing to extract features from the image, which will be the basement for the Optical Flow calculation.
To solve the problem of sparse optical flow we have employed Lucas-Kanade algorithm:


Lucas-Kanade algorithm:

The Lucas-Kanade method is commonly used to calculate the Optical Flow for a sparse feature set. The main idea of this method based on a local motion constancy assumption, where nearby pixels have the same displacement direction. This assumption helps to get the approximated solution for the equation with two variables.


Theory:

Let’s assume that the neighboring pixels have the same motion vector ![image](https://user-images.githubusercontent.com/86003669/205465307-7a7ed527-46c3-4afd-bb1d-242fcb341eac.png). We can take a fixed-size window to create a system of equations. Let![image](https://user-images.githubusercontent.com/86003669/205465316-34dea72f-c474-467a-a944-95598f6202f6.png) be the pixel coordinates in the chosen window of n elements . Hence, we can define the equation system as:
![image](https://user-images.githubusercontent.com/86003669/205465329-56acc2af-e140-493e-bc1f-f59acf0e204f.png)

Rewriting in matrix form:

![image](https://user-images.githubusercontent.com/86003669/205465340-5b7a272e-b53a-4efd-a47d-6cdaa950ba31.png)

Now we have a amtrix equation of format ![image](https://user-images.githubusercontent.com/86003669/205465356-4b16f370-96a0-49b2-bec7-40e31c7f8de1.png)
Therefore,
![image](https://user-images.githubusercontent.com/86003669/205465369-1838655f-47c0-4f89-af00-20eb92a4e991.png)

i.e. gamma is equal to pseudoinverse of A multiplied by b.

The Lucas Kanade algorithm usually suffers from some abrupt movements due to limitaion of optical flow strategy. Now to imporve this algorithm we used the function goodFeaturesToTrack(). This function is used to find N strongest corners in the image to track by either Shi-Tomasi or Harrison Corner detector.


Practical:
In the files attached above

Result Screenshot:
![image](https://user-images.githubusercontent.com/86003669/205465706-6b112177-1c3d-4b5a-b89c-a1c126cf13a7.png)



Optical Flow applications:
Optical Flow can be used in many areas where the object’s motion information is crucial. Optical Flow is commonly found in video editors for compression, stabilization, slow-motion, etc. Also, Optical Flow finds its application in Action Recognition tasks and real-time tracking systems.
