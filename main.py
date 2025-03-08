from csv import writer
from datetime import datetime
import cv2
import face_recognition
import numpy as np

# Initialize the video capture
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Load known faces and their encodings
known_face_encodings = []
known_face_names = []

# Add your known images here
students_data = {
    "santosh": "santosh.jpg",
    "utkarsh": "utkarsh.jpg",
    "aniket": "aniket.jpg",
    "arvind kumar": "arvind.jpg",
    "rishav":"rishav.jpg",
    "ayush": "ashush.jpg"
}

for name, filename in students_data.items():
    try:
        image = face_recognition.load_image_file(filename)
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(name)
    except Exception as e:
        print(f"Error loading {filename}: {e}")

# List of students who haven't been marked present yet
students = known_face_names.copy()

# Get current date for CSV filename
now = datetime.now()
current_date = now.strftime("%Y-%m-%d_%H-%M-%S")

# Open CSV file for writing attendance
try:
    f = open(f"{current_date}.csv", "w+", newline="")
    lnwriter = writer(f)
    lnwriter.writerow(["Name", "Time"])  # Add headers
except Exception as e:
    print(f"Error creating CSV file: {e}")
    video_capture.release()
    cv2.destroyAllWindows()
    exit()

print("Attendance System is Running...")

try:
    while True:
        # Capture frame from the camera
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Recognize faces
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Check for a match with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            name = "Unknown"
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # Draw a dark blue box around the face
            top, right, bottom, left = face_location
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)  # Dark Blue rectangle

            # Display the name below the face
            if name != "Unknown":
                # Mark attendance if student is physically present and hasn't been marked yet
                if name in students:
                    students.remove(name)  # Ensure attendance is marked only once
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    lnwriter.writerow([name, current_time])
                    print(f"{name} marked present at {current_time}")

                # Show "Name Present" on the camera feed
                cv2.putText(frame, f"{name} Present", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)  # Dark Blue text

        # Display the resulting frame
        cv2.imshow("Attendance", frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up resources
    print("Exiting...")
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()
