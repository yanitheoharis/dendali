import cv2
import numpy as np
import mediapipe as mp


##Typical Preprocessing steps:
""" 
1. Resizing
2. Cropping
3. Denoising
4. Color Normalization / Histogram Equalization
5. Contrast Adjustment
6. Image Augmentation (For Training)
7. Image Color Conversion
8. Check for Image Orientation (Correcting Upside-Down Images)
9. Check Image Aspect Ratio """




class ImagePreprocessor:
    def __init__(self, image_path):
        # Load the image
        self.image = cv2.imread(image_path)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
        # self.mp_face_mesh = mp.solutions.face_mesh
        # self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5)
    
    def resize_image(self, width=224, height=224):
        """
        Resize image to desired dimensions
        """
        self.image = cv2.resize(self.image, (width, height))
        self.gray = cv2.resize(self.gray, (width, height))
    
    def normalize(self):
        """
        Normalize the image (scaling pixel values to [0, 1])
        """
        self.image = self.image.astype('float32') / 255.0
    
    def equalize_histogram(self):
        """
        Apply histogram equalization to enhance contrast
        """
        self.gray = cv2.equalizeHist(self.gray)
    
    # def detect_face(self):
    #     """
    #     Detect faces in the image
    #     """
       
        
    #     faces = self.face_cascade.detectMultiScale(self.gray, scaleFactor=1.3, minNeighbors=5)
    #     for (x, y, w, h) in faces:
    #         # Draw rectangle around the face
    #         cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #         self.face_roi = self.image[y:y + h, x:x + w]
    #         return self.face_roi
    #     return None
    
    # def detect_smile(self):
    #     """
    #     Detect smiles (and by extension, teeth) in the face region
    #     """
    #     if hasattr(self, 'face_roi'):
    #         gray_roi = cv2.cvtColor(self.face_roi, cv2.COLOR_BGR2GRAY)
    #         smiles = self.smile_cascade.detectMultiScale(gray_roi, scaleFactor=1.8, minNeighbors=20)
    #         for (sx, sy, sw, sh) in smiles:
    #             # Draw rectangle around the smile
    #             cv2.rectangle(self.face_roi, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
    #         return self.face_roi
    #     return None
    
    # def detect_landmarks(self):
    #     """
    #     Use MediaPipe to detect landmarks (mouth area for teeth inference)
    #     """
    #     image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
    #     results = self.face_mesh.process(image_rgb)
    #     if results.multi_face_landmarks:
    #         for landmarks in results.multi_face_landmarks:
    #             for i in range(78, 88):  # Mouth landmarks for teeth
    #                 x = int(landmarks.landmark[i].x * self.image.shape[1])
    #                 y = int(landmarks.landmark[i].y * self.image.shape[0])
    #                 cv2.circle(self.image, (x, y), 2, (0, 255, 0), -1)
    #         return self.image
    #     return None
    
    def convert_to_gray(self):
        """
        Convert the image to grayscale
        """
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return self.gray_image

    def convert_to_rgb(self):
        """
        Convert the image to RGB (OpenCV uses BGR by default)
        """
        self.rgb_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        return self.rgb_image
    
    def show_image(self, title="Processed Image"):
        """
        Display the processed image
        """
        cv2.imshow(title, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_processed_image(self):
        """
        Return the processed image
        """
        return self.image

