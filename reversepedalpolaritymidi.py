import os 
from mido import Message, MidiFile, MidiTrack
import sys






def process(filename):
    mid = MidiFile(filename)
    for track in mid.tracks:
       for i, msg in enumerate(track):
            if msg.type == 'control_change':
                ped = msg.value
                pedfix = abs(ped-127)
                # Replace message in track.                                         
                track[i] = msg.copy(value=pedfix)

    mid.save('*' + filename)


for f in os.listdir('.'):
    process(f)
