from collections import Counter
import re

# leer texto generado por speech_to_text
with open("output/transcription.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

muletillas = [
    "este",
    "osea",
    "bueno",
    "entonces",
    "literalmente",
    "tipo"
]

palabras = re.findall(r'\b\w+\b', texto.lower())

conteo = Counter(p for p in palabras if p in muletillas)

print("\nMULETILLAS DETECTADAS:\n")

if conteo:
    for muletilla, cantidad in conteo.items():
        print(f"{muletilla}: {cantidad}")
else:
    print("No se detectaron muletillas.")
    