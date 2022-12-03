import sys
import numpy as np

import time
import cv2
from matplotlib import pyplot as plt 



lk_params = dict( winSize  = (5, 5),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 10,
                       blockSize = 10 )

traj_len = 120   # we will have 20 points in each trajectory for each point to be tracked
detect_interval = 1  # how often we want to uodate corners
trajectories = []
frame_idx = 0   


cap = cv2.VideoCapture("/home/rob502/Downloads/Pexels Videos 2053100.mp4")

# Take the first frame and assign it as old_frame

result = cv2.VideoWriter('dhyey_OP_final.mp4',cv2.VideoWriter_fourcc(*'MJPG'),10, (1000,1000))

while True:

    # FPS timer
    start = time.time()

    
    suc , frame = cap.read() 
    if not suc:
        print('Error : No frames')
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = frame.copy()




    if(len(trajectories)>0):

        img0,img1 = prev_gray,frame_gray

        p0 = np.float32([trajectory[-1] for trajectory in trajectories]).reshape(-1,1,2)
        # p0 = cv2.goodFeaturesToTrack(img0,mask=None,**feature_params)
        p1, st, err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)
        p01, st, err = cv2.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)

        

        diff = abs(p0-p01).reshape(-1, 2).max(-1)
        good = diff < 1


        new_trajectories = []


            
        for trajectory,(x,y), good_flags in zip(trajectories, p1.reshape(-1,2), good):
            if not good_flags:
                continue
            else:
                trajectory.append((x,y))
                if len(trajectory) > traj_len:
                    del trajectory[0]
            
            new_trajectories.append(trajectory)

        

        cv2.polylines(img, [np.int32(trajectory) for trajectory in trajectories], False, (0, 255, 0)) 

            
        cv2.putText(img, "Trajectory Count w.r.t. FPS : %d" %len(trajectories), (100,100),cv2.FONT_HERSHEY_SIMPLEX, fontScale = 2, color = (0,250,0), thickness = 3)





    
    if frame_idx%detect_interval ==0:
        mask = np.zeros_like(frame_gray)
        mask[:] = 255

        for x,y in [np.int32(trajectory[-1]) for trajectory in trajectories]:
             cv2.circle(mask, (x,y), 5, (255,0,0), -1)
             
        p = cv2.goodFeaturesToTrack(frame_gray,mask=mask,**feature_params)

        if p is not None:
           for x,y in np.float32(p).reshape(-1,2):
                trajectories.append([(x,y)])

    frame_idx = frame_idx + 1
    prev_gray = frame_gray


    end = time.time()

    fps = 1/(end-start)
    cv2.putText(img, f"{fps:.2f} FPS", (20,20),cv2.FONT_HERSHEY_SIMPLEX, fontScale = 2, color = (0,250,0), thickness = 3)

    cv2.imshow("OPTICAL FLOW",img)




    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    # # Now update the previous frame and previous points
    # old_gray = frame_gray.copy()
    # p0 = good_new.reshape(-1, 1, 2)


cap.release()
result.release()
cv2.destroyAllWindows()

