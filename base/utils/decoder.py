import cv2
import numpy as np
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

def Decoder(image_b:bytes) -> str:
    try:
        image = np.frombuffer(image_b,np.uint8)
        image = cv2.imdecode(image,cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imwrite("output.jpg",image)
        
        image_path = "output.jpg" 
        qr_codes_data = read_qr_code(image_path)
        if qr_codes_data:
            print("QR Code(s) found:")
            return qr_codes_data[0]

    except Exception as e:
        print("Found Error in Decoder: ")
        print(e)
    
    return("Could not find the given QR Code")
        