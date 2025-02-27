import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_face_mesh=mp.solutions.face_mesh

drawing_spec=mp_drawing.DrawingSpec(color =(100,0,355), thickness=1,circle_radius=1)

cap=cv2.VideoCapture(0)

# Temporarily change the values
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5,
                           min_tracking_confidence=0.5) as face_mesh:
    
    while True:
        ret,frame=cap.read()
        img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img.flags.writeable=False

        results=face_mesh.process(img)
        print(results)

        img.flags.writeable=True
        img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(image=img,
                                          landmark_list=face_landmarks,
                                          landmark_drawing_spec=drawing_spec,
                                          connection_drawing_spec=drawing_spec)
        
        cv2.imshow("Mesh",img)
        if (cv2.waitKey(30)==ord("s")):
            break

    cap.release()
    cv2.destroyAllWindows()
