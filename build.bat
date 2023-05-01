python -m pip install -r requirements.txt
pyinstaller --noconfirm --onefile --windowed --icon "%CD%\racik.ico" --add-data "%CD%\ffmpeg;ffmpeg"  "%CD%\jumpscare.py"
pyinstaller --noconfirm --onefile --windowed --icon "%CD%\racik.ico" --add-data "%CD%\templates;templates" --add-data "%CD%\static;static" --add-data "%CD%\quiet.exe;." --add-data "%CD%\dist\jumpscare.exe;."  "%CD%\main.py"