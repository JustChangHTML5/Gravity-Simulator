rm -rf dist build
#pyinstaller --onefile main.py
pyinstaller --onefile -w main.py
copy *.png dist
copy *.mp3 dist
copy *.jpg dist