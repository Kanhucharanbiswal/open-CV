import cv2 

image = cv2.imread("Image Drawing Function\Stu.jpg")

if image is None:
    print("Opps! Your image is not working")

else:
    print("Image loaded sucessfully!")
    cv2.circle(image, (150,150), 50, (255,0,0), -1)

    cv2.imshow("Drawing Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()