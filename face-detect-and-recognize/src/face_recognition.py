import cv2

# Initialize video capture from the webcam
video_capture = cv2.VideoCapture(0)

# Load the Haar cascade for face detection
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = video_capture.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,   # Parameter specifying how much the image size is reduced at each image scale
        minNeighbors=5,    # Parameter specifying how many neighbors each candidate rectangle should have to retain it
        minSize=(30, 30)   # Minimum possible object size. Objects smaller than that are ignored
    )

    # Print the number of faces found
    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
