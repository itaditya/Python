import cv2
import sys
# import imutils
# Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"


# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
# help(faceCascade)
# Read the image
image = cv2.imread(imagePath)
image = cv2.resize(image, (min(1400, image.shape[1]), min(
    800, image.shape[0])), interpolation=cv2.INTER_CUBIC)
print(image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=3,
    minSize=(10, 10),
    maxSize=(100, 100)
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
