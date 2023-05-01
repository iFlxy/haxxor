python3 -m pip install -r requirements.txt
pyinstaller --noconfirm --onefile --windowed  "./jumpscare.py"
pyinstaller --noconfirm --onefile --windowed --add-data "./templates:templates/" --add-data "./static:static/" --add-data "./dist/jumpscare:."  "./main.py"