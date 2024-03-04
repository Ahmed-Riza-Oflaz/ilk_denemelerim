import cv2

def convert_to_black_and_white(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, convert_to_black_and_white_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    cv2.imwrite(output_image_path, convert_to_black_and_white_image)

input_path = "cv_denemesi.png"
output_path = "cv_deneme_sonuc.jpg"

convert_to_black_and_white(input_path, output_path)

