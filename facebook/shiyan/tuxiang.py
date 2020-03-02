import cv2

img=cv2.imread('1.jpg')
cv2.namedWindow("iiiiii")
cv2.imshow("iiiiii",img)

cv2.putText(img,'5120147157',(50,150),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,255),18)
cv2.imshow("iiii",img)
cv2.imwrite('2.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()