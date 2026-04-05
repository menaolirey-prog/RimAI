# RimAI – Prototipo de análisis de comunicación

RimAI es un prototipo que permite analizar la calidad de la comunicación oral mediante el procesamiento automático de audio.

El sistema convierte audio en texto y luego identifica patrones como muletillas, que pueden afectar la claridad y fluidez del discurso.

---

## Arquitectura del prototipo

Flujo del sistema:

audio → texto → detección de muletillas

---

## Scripts incluidos

### 1. speech_to_text.py

Convierte un archivo de audio (.wav) en texto utilizando reconocimiento de voz offline mediante el modelo Vosk.

Entrada:
audio.wav

Salida:
transcription.txt

Este módulo permite transformar contenido hablado en texto para su posterior análisis.

---

### 2. filler_detector.py

Analiza el texto generado y detecta muletillas frecuentes en el discurso.

Ejemplos de muletillas detectadas:

- este
- osea
- bueno
- entonces
- tipo
- literalmente

Este análisis permite evaluar la fluidez de la comunicación.


## Objetivo del prototipo

El objetivo de RimAI es desarrollar una herramienta que permita evaluar la claridad de la comunicación oral en contextos profesionales, educativos y corporativos.

El sistema puede utilizarse como base para:

- evaluación de habilidades comunicativas
- entrenamiento en presentaciones
- mejora de claridad en el discurso
- análisis de entrevistas
- retroalimentación automatizada

---

## Tecnologías utilizadas

- Python
- Vosk Speech Recognition
- Procesamiento de lenguaje natural (NLP)
