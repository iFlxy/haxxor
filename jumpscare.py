import os
import sys
import moviepy.config as movieconf
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
if sys.platform == "win32":
	movieconf.FFMPEG_BINARY = os.path.join(resource_path("ffmpeg"), "bin", "ffmpeg.exe")

from pygame import mixer
import cv2
import shutil
import tempfile
from moviepy.editor import *
import requests

temp_dir = tempfile.gettempdir()

output = open(os.path.join(temp_dir, 'logs.txt'), "wt")
sys.stdout = output
sys.stderr = output

try:
	os.remove(os.path.join(temp_dir, 'video.mp4'))
	os.remove(os.path.join(temp_dir, 'music.mp3'))
except:
	print("dupa")

try:
    url = sys.argv[1]
except:
    sys.exit()
temp_file = tempfile.NamedTemporaryFile(delete=False)
response = requests.get(url)
temp_file.write(response.content)
temp_file.close()

shutil.copy(temp_file.name, os.path.join(temp_dir, 'video.mp4'))
video = VideoFileClip(os.path.join(temp_dir, 'video.mp4'))
video.audio.write_audiofile(os.path.join(temp_dir, 'audio.mp3'))

mixer.init()

file_name = os.path.join(temp_dir, 'video.mp4')
window_name = "szczurek"
interframe_wait_ms = 32

mixer.music.load(os.path.join(temp_dir, 'audio.mp3'))


cap = cv2.VideoCapture(file_name)
cap.set(cv2.CAP_PROP_FPS, 60)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)

frame_counter = 0

mixer.music.play(loops = -1)

while (True):
	ret, frame = cap.read()
	frame_counter += 1
	if cv2.waitKey(25) & 0xFF == ord('q'):
		print("dupa")
	if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
		frame_counter = 0
		cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
		sys.exit()

	cv2.imshow(window_name, frame)
cap.release()
cv2.destroyAllWindows()