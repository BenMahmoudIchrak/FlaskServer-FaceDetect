import face_recognition
import os
import sys
import cv2
import numpy as np
import math

from flask import Flask, jsonify
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



def face_confidence(face_distance, face_match_threshold=0.6):
    range_ = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range_ * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'

class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True

    def __init__(self):
        self.encode_faces()

    def encode_faces(self):
        for image in os.listdir('faces'):
            face_image = face_recognition.load_image_file(f'faces/{image}')
            face_encoding = face_recognition.face_encodings(face_image)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(image)

        print(self.known_face_names)

    def run_recognition(self):
        name = ''
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            sys.exit('Video source not found...')

        while True:
            ret, frame = video_capture.read()

            if ret:
                if self.process_current_frame:
                    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                    rgb_small_frame = small_frame[:, :, ::-1]

                    self.face_locations = face_recognition.face_locations(rgb_small_frame)
                    self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                    self.face_names = []
                    for face_encoding in self.face_encodings:
                        matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                        name = 'Unknown'
                        confidence = 'Unknown'

                        face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances)

                        if matches[best_match_index]:
                            name = self.known_face_names[best_match_index]
                            confidence = face_confidence(face_distances[best_match_index])

                        self.face_names.append(f'{name} ({confidence})')

                    if self.face_names:
                        name = self.face_names[0].split(' ')[0]  # Prend le nom sans la confidence
                        break  # Sort de la boucle dès qu'une reconnaissance est faite

                self.process_current_frame = not self.process_current_frame

        video_capture.release()
        cv2.destroyAllWindows()

        return name


fr = FaceRecognition()

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Face Recognition API!"

@app.route('/encode_faces', methods=['GET'])
def encode_faces():
    fr.encode_faces()
    return jsonify({'message': 'Faces encoded successfully'}), 200

@app.route('/run_recognition', methods=['GET'])
def run_recognition():
    name = fr.run_recognition()  # Obtenez le nom de la personne détectée
    return jsonify({'message': 'Recognition completed successfully', 'name': name}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)