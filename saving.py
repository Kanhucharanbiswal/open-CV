import cv2

image = cv2.imread("images\Photos\Bike.png")

if image is not None:
    success = cv2.imwrite("output_Bike.png", image)
    if success:
        print("Image saved succesfully as 'output_Bike.png'")
    else:
        print("Failed to save an image")

else:
    print("Error:could not load image")  