import cv2

image = cv2.imread("images\Photos\Bike.png")

if image is None:
    print("Could not load image")

else:
    print("Image loaded successfully")
