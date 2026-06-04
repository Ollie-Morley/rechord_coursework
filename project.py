# imports of libraries
#  j
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sounddevice as sd
import numpy as np
import time
import os
import soundfile as sf
from pedalboard import Pedalboard, Reverb, Delay, Chorus, Distortion, Compressor
from pedalboard.io import AudioFile


'''
global variables
'''
bg = 'black'
login = False
valid = False

'''
Project idea, open source audio sampling, think splice but open to everyone rather than just artists.
'''
'''
Procedures/functions

'''
'''
fx fucntion, not sure if its gonna be used yet
def apply_fx(board, file_search_enter):
    with AudioFile(file_search_enter.get()) as f:
        while f.tell() < f.frames:
            chunk = f.read(f.samplerate)
            effected = board(chunk, f.samplerate, reset=False)
            f.write(effected)
            sd.play(effected, f.samplerate)
            sd.wait()

def fx(root):
    board = Pedalboard([Chorus(), Reverb(room_size=0.25)])
    file_search_label = tkinter.Label(root, text='Enter the name of the file to be processed: ', bg=bg, fg='grey')
    file_search_label.pack()
    file_search_enter = tkinter.Entry(root)
    file_search_enter.pack()
    file_search_but = tkinter.Button(root, text='Apply FX', bg='grey', fg=bg) 
    file_search_but.pack()
    with AudioFile(file_search_enter.get()) as f:
        while f.tell() < f.frames:
            chunk = f.read(f.samplerate)
            effected = board(chunk, f.samplerate, reset=False)
            f.write(effected)


'''

def search_file(the_box):

    samplerate = 44100
    file_name = the_box.get()
    if file_name == 'Select a file to load':
        messagebox.showerror('Error', 'Please select a file to load')
    else:
        print('works')
        file_name = file_name.replace(', ', '')
        
    data, samplerate = sf.read(file_name)
    sd.play(data, samplerate)
    sd.wait()



def search(root):


    directory_path = r"/Users/olivermorley/Desktop/Coursework"
    file_type = ".wav"

    file_title = []
    for dirpath, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(file_type):
                full_path = os.path.join(dirpath, file)
                audio_name = full_path.replace('Users/olivermorley/Desktop/Coursework/', '')
                audio_name = audio_name.replace('/', '')
                file_title.append(audio_name + ', ')
    

    #print(file_title)
    the_box = ttk.Combobox(root, values=file_title)
    the_box.set('Select a file to load') 
    the_box.pack()
    save_button = Button(root, text='Select file', bg='grey', fg=bg, command=lambda: search_file(the_box))
    save_button.pack()
 
    



def record(root, valid, duration, named):
    sample_r=44100


    record_label = tkinter.Label(root, text='Recording Finished', bg=bg, fg='white')
    record_label.pack()
    
    recording = sd.rec(int(duration * sample_r), samplerate=sample_r, channels=1)
    sd.wait()
    print('Recording complete')
    #sd.play(recording, sample_r)
    if valid == True:
        save_label = tkinter.Label(root, text='Saving recording as ' + named + '.wav', bg=bg, fg='white')
        save_label.pack()
        print('Saving recording as ' + named + '.wav')
        path = '/Users/olivermorley/Desktop/Coursework'
        sf.write(path + '/' + named + '.wav', recording, sample_r)
    else:
        error_label = tkinter.Label(root, text='Recording could not be processed \n Please enter a valid name for the file', bg=bg, fg='white')
        error_label.pack()


def validation(len_enter, name_enter, root, valid):
    
    if len_enter.get() == '' or len_enter.get().isdigit() == False:
        len_presence = tkinter.Label(root, text='Please enter a valid length for recording', bg=bg, fg='white')
        len_presence.pack()
        #validation(len_enter, name_enter, root, valid)
    else:
        duration = int(len_enter.get())
        valid = True

    
    named = str(name_enter.get())
    if named == '':
        presence_label = tkinter.Label(root, text='Please enter a name for the file', bg=bg, fg='white')
        presence_label.pack()
        valid=False
        #validation(len_enter, name_enter, root, valid)
    elif named != '':
        valid = True

        record(root, valid, duration, named)


# login method, implemment later.
'''
file = open('users.txt', 'r')
users = file.read().splitlines()
print(users)
'''

'''
while login == False:

    user = input('Enter username: ')
    password = input('Enter unique code: ')
    for lines in users:
        if user == lines.split(',')[0] and password == lines.split(',')[1]:
            login = True
            break
        if login == False:
            print('Invalid user or login code \n Please try again')
'''



root = tkinter.Tk()
root.title('Audio project')

root.attributes('-fullscreen', True)
root.configure(bg=bg)
title_label = tkinter.Label(root, text='ReChord', font=('Arial', 50), bg=bg, fg='white')
title_label.pack()

len_label = tkinter.Label(root, text='Enter recording length(s):', bg=bg, fg='white')
len_label.pack()
len_enter = tkinter.Entry(root)
len_enter.pack()

name_label = tkinter.Label(root, text='Enter the name of the file to be saved as: ', bg=bg, fg='white')
name_label.pack()
name_enter = tkinter.Entry(root)
name_enter.pack()

record_but = tkinter.Button(root, text='Record', bg='grey', fg=bg, command=lambda: validation(len_enter, name_enter, root, valid))
record_but.pack()
space = tkinter.Label(root, text='\n', bg=bg)
space.pack()

search_button = tkinter.Button(root, text='Search for audio', fg=bg, bg='grey', command =lambda: search(root))
search_button.pack()
'''
fx_but = tkinter.Button(root, text='Choose file for FX.', bg='grey', fg=bg, command=lambda: fx(root))
fx_but.pack()
'''
space2 = tkinter.Label(root, text='\n', bg=bg)
space2.pack()
exit_but = tkinter.Button(root, text='Exit', bg="grey", fg='#9E0707', command=root.destroy)
exit_but.pack()


'''
insert buttons for audio to play 

'''





'''
procedure calls sss
'''


root.mainloop()