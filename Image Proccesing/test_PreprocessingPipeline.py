import unittest
import cv2
from PreprocessingPipeline import ImagePreprocessor 
import numpy as np

class TestImagePreprocessor(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment. This method will be run before each test.
        """
        self.image_path = 'data1.jpg'
        self.preprocessor = ImagePreprocessor(self.image_path)

    def test_resize_image(self):
        """
        Test image resizing functionality.
        """
        original_shape = self.preprocessor.image.shape
        self.preprocessor.resize_image(256, 256)
        resized_shape = self.preprocessor.image.shape
        self.assertEqual(resized_shape, (256, 256, 3), f"Expected (256, 256, 3) but got {resized_shape}")
        
    def test_normalize(self):
        """
        Test image normalization to ensure pixel values are between [0, 1].
        """
        self.preprocessor.normalize()
        self.assertTrue(np.all(self.preprocessor.image <= 1.0), "Pixel values are greater than 1")
        self.assertTrue(np.all(self.preprocessor.image >= 0.0), "Pixel values are less than 0")

    def test_equalize_histogram(self):
        """
        Test histogram equalization.
        """
        original_mean = np.mean(self.preprocessor.gray)
        self.preprocessor.equalize_histogram()
        equalized_mean = np.mean(self.preprocessor.gray)
        self.assertNotEqual(original_mean, equalized_mean, "Histogram equalization did not change the image")

    # def test_detect_face(self):
    #     """
    #     Test face detection. The result should be a face ROI.
    #     """
    #     face_roi = self.preprocessor.detect_face()
    #     self.assertIsNotNone(face_roi, "No face detected in the image")

    # def test_detect_smile(self):
    #     """
    #     Test smile detection. If a smile is detected, the result should have a rectangle drawn around it.
    #     """
    #     self.preprocessor.detect_face()  # First, detect the face
    #     face_with_smile = self.preprocessor.detect_smile()
    #     self.assertIsNotNone(face_with_smile, "Smile detection failed. No smile detected.")

    # def test_detect_landmarks(self):
    #     """
    #     Test landmark detection for the mouth region.
    #     """
    #     landmarks_image = self.preprocessor.detect_landmarks()
    #     self.assertIsNotNone(landmarks_image, "Landmarks not detected in the image")
    def test_convert_to_gray(self):
        """
        Test conversion of image to grayscale
        """
        gray_image = self.preprocessor.convert_to_gray()
        self.assertEqual(len(gray_image.shape), 2, "Grayscale image should have only 2 dimensions (height and width)")
    
    def test_convert_to_rgb(self):
        """
        Test conversion of image to RGB
        """
        rgb_image = self.preprocessor.convert_to_rgb()
        self.assertEqual(rgb_image.shape[2], 3, "RGB image should have 3 channels")


    def test_show_image(self):
        """
        Test the image display functionality. This should open an image window.
        """
        
        try:
            self.preprocessor.show_image("Test Image Display")
        except Exception as e:
            self.fail(f"show_image() raised {type(e).__name__} unexpectedly!")

    def tearDown(self):
        """
        Clean up after each test.
        """
        pass  

if __name__ == "__main__":
    unittest.main()
