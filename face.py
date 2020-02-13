import numpy as np
import cv2

## TODO add frames/sec dependence

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

class Face():

###############################################################
# @Function: __init__()                                       #
# @Param   : 'camera_id', the camera id used for opencv       #
# @Returns : 'void'                                           #
###############################################################
    def __init__(self, camera_id = 0):
        self.cap = cv2.VideoCapture(camera_id)
        ## TODO use the score to filter multiple images
        score = 0


###############################################################
# @Function: detect_eyes()                                    #
# @Param   : 'cvt_gray': returns gray eyes if set to True     #
# @Returns : 'eyes_list', list of the two eyes                #
###############################################################
    def detect_eyes(self, cvt_gray=False):
        self.cvt_gray = cvt_gray
        _, img = self.cap.read()
        if(img == None):
            img = cv2.imread('Non-Existing Person.jpg')
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        eyes_list = []
        # if a face is found
        if(len(faces)!=0):
            for (x,y,w,h) in faces:
                print('face found!')
                #cv2.rectangle(img,(x,y),(x+w,int((y+h)/1.5)),(255,0,0),2)
                roi_gray = gray[y:int((y+h)/1.5), x:x+w]
                roi_color = img[y:int((y+h)/1.5), x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                # if an eye is found
                if(len(eyes)!=0):
                    print('eyes found!')
                    for (ex,ey,ew,eh) in eyes:
                        #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,0),1)
                        #print(ex,ey,ew,eh)
                        if(cvt_gray):
                            eyes_list.append(roi_gray[ey:ey+eh, ex:ex+ew])
                        else:
                            eyes_list.append(roi_color[ey:ey+eh, ex:ex+ew])

                else:
                    print('no eyes found!')
                    ## TODO Add a solution when no eye is detected in the face 
                    #cv2.rectangle(roi_color,(x,y),(x+w,y+h),(0,0,0),1)
                    eyes_list.append(img[y:y+h, x:int((x+w)/2)])
                    eyes_list.append(img[y:y+h, int((x+w)/2):x+w])

        else:
            print('no face found')
            # return zeros if no face is detected
            eyes_list.append(np.zeros_like(img))
            eyes_list.append(np.zeros_like(img))

        return eyes_list
