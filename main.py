import cv2
import pytesseract



if __name__ == '__main__':
    img = cv2.imread("1.png")
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply threshold to convert to binary image
    threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    cv2.imwrite("output.jpg",threshold_img)

    # Pass the image through pytesseract
    text = pytesseract.image_to_string(threshold_img)

    # Print the extracted text
    print("Extracted text: ")
    print(text)
