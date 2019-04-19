import time
import os
import cv2
from shutil import copyfile
import subprocess
import socket


def main():
	while True:
		takeImage()
		os.system("python3 detect.py --image_folder captures")
		copyfile("objects.txt", "../hello-world-tutorial/public/objects.txt")

def takeImage():
	cam = cv2.VideoCapture(0)
	cv2.namedWindow("test")
	ret, frame = cam.read()
	cv2.imshow("test", frame)
	cv2.imwrite("captures/capture.jpg", frame)
	cam.release()
	cv2.destroyAllWindows() 

if __name__ == "__main__":
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('172.20.10.12', 10000))
	data = b''
	while True:
		buff = sock.recv(1)
		if data == b'start':
			print("starting dashboard")
			break
		else:
			data += buff

	p = os.path.dirname(os.path.abspath(__file__))
	subprocess.Popen("npm start", shell=True, stdout = subprocess.PIPE, cwd= p + "/../hello-world-tutorial")
	main()
