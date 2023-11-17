import soundfile as sf
import os
import sys
from glob import glob

sys.path.append('.')

duration = 0.0
wav_count = 0

singers = [x[0] for x in os.walk('.')]
print(singers)
time_dict = {}

for i in range(len(singers)):
    for wav in glob(os.path.join(singers[i], '*.wav')):
        f = sf.SoundFile(wav)
        duration += float(f.frames) / float(f.samplerate)

    minutes = duration/60

    if minutes > 60:

        if minutes > 120:
            min2 = minutes - 120
            hours = str(2) + ':' + str(min2)
        elif minutes > 180:
            min2 = minutes - 180
            hours = str(3) + ':' + str(min2)
        elif minutes > 240:
            min2 = minutes - 240
            hours = str(4) + ':' + str(min2)
        elif minutes > 60:
            min2 = minutes - 60
            hours = str(1) + ':' + str(min2)
        else:
            minutes = str(minutes)

    time_dict[singers[i][3:]] = minutes

out_text = 'Dataset Timed\n'
for key in time_dict:
    out_text += '%s : %s\n' % (key, time_dict[key])

with open(os.path.join('.') + 'timed.txt', 'w') as out_file:
    out_file.write(out_text)