import cv2
import numpy as np


def Decoder(image_b:bytes) -> str:
    try:
        image = np.frombuffer(image_b,np.uint8)
        image = cv2.imdecode(image,cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imwrite("output.jpg",image)
        print("done writing")
        detector = cv2.QRCodeDetector()
        data, vertices_array, binary_data = detector.detectAndDecode(image)

        if(vertices_array is not None):
            print("Decoded The given QR code of len-v")
            print(len(data))
            print(data)

            return data
        else:
            print("Could not find the given QR Code")
    except Exception as e:
        print("Found Error in Decoder: ")
        print(e)
    
    return("Could not find the given QR Code")
        