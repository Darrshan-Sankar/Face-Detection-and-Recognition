import face_recognition
import cv2
import os

# Path to the folder containing the images of persons
persons_folder = "persons_data"

# Load images and encode faces
known_face_encodings = []
known_face_names = []

for person_image_file in os.listdir(persons_folder):
    person_name = os.path.splitext(person_image_file)[0]  # Extract person name from filename
    person_image_path = os.path.join(persons_folder, person_image_file)
    person_image = cv2.imread(person_image_path)
    person_face_encoding = face_recognition.face_encodings(person_image)[0]  # Assuming only one face per image
    known_face_encodings.append(person_face_encoding)
    known_face_names.append(person_name)

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to capture frame")
        break

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Iterate through each face found in the frame
    for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        # Compare the face encoding with known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # Find the index of the first match (if any)
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a rectangle around the face and label it with the person's name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
