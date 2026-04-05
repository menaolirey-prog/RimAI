# RimAI# RimAI – Speech Analysis Prototype

Prototype developed to analyze spoken communication quality.

## Scripts

### 1. speech_to_text.py
Converts audio (.wav) into text using Vosk speech recognition.

Input:
audio.wav

Output:
transcription.txt

### 2. filler_detector.py
Detects filler words in speech such as:

- este
- osea
- bueno
- entonces
- tipo
- literalmente

## Pipeline

audio → text → filler detection

## Objective

Help evaluate communication clarity and reduce filler words in professional environments.
