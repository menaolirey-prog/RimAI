
from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import json

SetLogLevel(-1)

model = Model(r"model\vosk-model-small-es-0.42")
wf = wave.open(r"input\audio.wav", "rb")

rec = KaldiRecognizer(model, wf.getframerate())
texto_final = ""

while True:
    data = wf.readframes(8000)
    if len(data) == 0:
        break

    if rec.AcceptWaveform(data):
        resultado = json.loads(rec.Result())
        texto_final += resultado.get("text", "") + " "

resultado_final = json.loads(rec.FinalResult())
texto_final += resultado_final.get("text", "")

print("\nTEXTO DETECTADO:\n")
print(texto_final.strip())
with open("output/transcription.txt", "w", encoding="utf-8") as f:
    f.write(texto_final.strip())

print("\nArchivo guardado en output/transcription.txt")