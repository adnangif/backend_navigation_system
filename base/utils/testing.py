import cv2
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Decode QR code
    decoded_objects = decode(gray_image)

    # Extract data from decoded objects
    qr_codes_data = [obj.data.decode('utf-8') for obj in decoded_objects]
    
    return qr_codes_data

if __name__ == "__main__":
    image_path = "output.jpg"  # Change this to your image path
    qr_codes_data = read_qr_code(image_path)
    if qr_codes_data:
        print("QR Code(s) found:")
        for data in qr_codes_data:
            print(data)
    else:
        print("No QR Code found in the image.")
