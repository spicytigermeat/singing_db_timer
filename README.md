# Singing DB Timer 🎵

## Usage
Ensure you have set your directory to the root folder, containing subdirectories of wav files of singing. Please not this will not read any wav files in the root folder!

Install dependencies!
```
pip install -r requirements.txt
```
(or just `pip install soundfile`)

Folder Structure:
```
root
|  voice1
|  |  song1.wav
|  |  song2.wav
|  |  song3.wav
|  voice2
|  |  song1.wav
|  |  song2.wav
|  |  song3.wav
```
To run the script:
```
python timer_out.py
```

Output is saved as `timed.txt` in root folder!

Please see releases for a portable, .exe version of this!
