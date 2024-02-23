import cv2


if __name__ == '__main__':
    img = cv2.imread('test_1.jpeg')
    detector = cv2.QRCodeDetector()

    data, vertices_array, binary_qrcode = detector.detectAndDecode(img)

    if vertices_array is not None:
        print("QRCode data:")
        print(data)
    else:
        print("There was some error") 