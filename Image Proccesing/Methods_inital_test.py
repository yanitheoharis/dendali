from PreprocessingPipeline import ImagePreprocessor

# Example usage:
image_path = 'data1.jpg'
preprocessor = ImagePreprocessor(image_path)
preprocessor.resize_image(640, 640)
preprocessor.normalize()
preprocessor.equalize_histogram()
preprocessor.convert_to_gray()
preprocessor.convert_to_rgb()
# preprocessor.detect_face()
# preprocessor.detect_smile()
# preprocessor.detect_landmarks()
preprocessor.show_image()
