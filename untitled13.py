# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hsSmg1PmABJTarpxL7fl0NQ-Tcya4dwb
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    # Read the WAV file
    sample_rate, data = wavfile.read(wav_file)

    # Check if data is stereo or mono
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo

    # Create a spectrogram
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)  # Set x-axis limit
    plt.ylim(0, sample_rate / 2)           # Frequency range from 0 to Nyquist frequency
    plt.grid(True)
    plt.show()

# Example usage
wav_file_path = '/content/timbo-drumline-loop-103bpm-171091.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path)

!pip install gtts

from gtts import gTTS
import os

# Matnni belgilash
text = "정부가 우선적으로 해결 해야 할 과제는 물가 안정이다 이번 공연은 관객들의 뜨거운 호응을 얻었다"
text = "정부가 우선적으로 해결 해야 할 과제는 물가 안정이다 이번 공연은 관객들의 뜨거운 호응을 얻었다"
text = "정부가 우선적으로 해결 해야 할 과제는 물가 안정이다 이번 공연은 관객들의 뜨거운 호응을 얻었다"

# Ovoz yaratish (gTTS - Google Text-to-Speech)
language = 'en'  # Changed to English ('en')
tts = gTTS(text=text, lang=language, slow=False)
language = 'en'  # Changed to English ('en')
tts = gTTS(text=text, lang=language, slow=False)
language = 'en'  # Changed to English ('en')
tts = gTTS(text=text, lang=language, slow=False)

# Ovoz faylini saqlash
audio_file = "output.mp3"
tts.save(audio_file)
audio_file = "output.mp3"
tts.save(audio_file)
audio_file = "output.mp3"
tts.save(audio_file)

# Ovoz faylini tinglash (Google Colab-da)
from IPython.display import Audio
Audio(audio_file)
from IPython.display import Audio
Audio(audio_file)
from IPython.display import Audio
Audio(audio_file)

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    # Read the WAV file
    sample_rate, data = wavfile.read(wav_file)

    # Check if data is stereo or mono
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo

    # Create a spectrogram
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)  # Set x-axis limit
    plt.ylim(0, sample_rate / 2)           # Frequency range from 0 to Nyquist frequency
    plt.grid(True)
    plt.show()

# Example usage
wav_file_path = '/content/acoustic-guitar-loop-f-91bpm-132687.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path)

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    # Read the WAV file
    sample_rate, data = wavfile.read(wav_file)

    # Check if data is stereo or mono
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo

    # Create a spectrogram
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)  # Set x-axis limit
    plt.ylim(0, sample_rate / 2)           # Frequency range from 0 to Nyquist frequency
    plt.grid(True)
    plt.show()

# Example usage
wav_file_path = '/content/pianos-by-jtwayne-7-174717.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path)

!pip install gtts

from gtts import gTTS
import os

# Matnni belgilash
text = "정부가 우선적으로 해결 해야 할 과제는 물가 안정이다 이번 공연은 관객들의 뜨거운 호응을 얻었다"

# Ovoz yaratish (gTTS - Google Text-to-Speech)
language = 'en'  # Changed to English ('en')
tts = gTTS(text=text, lang=language, slow=False)

# Ovoz faylini saqlash
audio_file = "output.mp3"
tts.save(audio_file)


# Ovoz faylini tinglash (Google Colab-da)
from IPython.display import Audio
Audio(audio_file)

!pip install gtts

from gtts import gTTS
import os

# Matnni belgilash
text = "공장에서 일이 많이면  어떻게 하시겠습니까 ?"

# Ovoz yaratish (gTTS - Google Text-to-Speech)
language = 'en'  # Changed to English ('en')
tts = gTTS(text=text, lang=language, slow=False)

# Ovoz faylini saqlash
audio_file = "output.mp3"
tts.save(audio_file)


# Ovoz faylini tinglash (Google Colab-da)
from IPython.display import Audio
Audio(audio_file)

!pip install gtts

from gtts import gTTS
import os

# Matnni belgilash
text = "공장에서 일이 많이면  어떻게 하시겠습니까 ?"

# Ovoz yaratish (gTTS - Google Text-to-Speech)
language = 'en'  # Changed to English ('en')
tts = gTTS(text=text, lang=language, slow=False)

# Ovoz faylini saqlash
audio_file = "output.mp3"
tts.save(audio_file)


# Ovoz faylini tinglash (Google Colab-da)
from IPython.display import Audio
Audio(audio_file)