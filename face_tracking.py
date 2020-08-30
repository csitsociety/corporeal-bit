import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

from luma.core.render import canvas

def get_faces(frame, face_cascade):
	image = frame.array

	# Convert to gray to perform face detection
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Detect faces
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)

	face_array = []
	# Find centers of all faces
	for (x, y, w, h) in faces:
		face_array.append([x+(w/2), y+(h/2)])

	return face_array

def play(d, event):
	d.text = 'Loading camera...'

	# Load camera
	camera = PiCamera()
	camera.resolution = (320, 240)
	camera.framerate = 20
	rawCapture = PiRGBArray(camera, size=(320, 240))
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	time.sleep(0.1)

	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		faces = get_faces(frame, face_cascade)

		if len(faces) > 0:
			with canvas(d) as drw:
				for f in faces:
					x = 100-(f[0]/3.2)
					y = f[1]/15
					drw.rectangle((x, y, x+4, y+4), fill='white')
			#d.text = str(faces[0][0]) + ', ' + str(faces[0][1])
		else:
			d.text = 'No faces\ndetected'

		# clear the stream in preparation for the next frame
		rawCapture.truncate(0)

		if event.is_set():
			break
