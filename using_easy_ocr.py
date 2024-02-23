import requests
import easyocr
import cv2

def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

    # Apply adaptive thresholding
    thresholded_image = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

    # Invert the thresholded image
    inverted_image = cv2.bitwise_not(thresholded_image)
    cv2.imwrite('output.jpg',inverted_image)

    return inverted_image

def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully as '{file_name}'")
    else:
        print("Failed to download image")


if __name__ == '__main__':
    server_url = "http://192.168.72.210/capture"
    download_image(server_url,'fetched.jpg')

    inv = preprocess_image('fetched.jpg')

    reader = easyocr.Reader(['en']) 
    result = reader.readtext(inv)
    print(result)

    
    

