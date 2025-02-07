import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Load the image
image = cv2.imread('data2.jpg')
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Initialize Face Mesh
with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
    results = face_mesh.process(rgb_image)

    # Draw face landmarks
    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image, landmarks, mp_face_mesh.FACEMESH_TESSELATION)

cv2.imshow("Smile Detection using MediaPipe", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
