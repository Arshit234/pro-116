import cv2
solarImage=cv2.imread("solar-system.jpg")
cv2.imshow("solarImage",solarImage)
cv2.putText(solarImage,
             "sun",
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(solarImage,
             "mercury",
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(solarImage,
             "venus",
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(solarImage,
             "earth",
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(solarImage,
             "mars",
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(solarImage,
             "jupiter",
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(solarImage,
             "saturn",
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(solarImage,
             "uranus",
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(solarImage,
             "neptune",
             (20,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )
cv2.waitKey(0)
