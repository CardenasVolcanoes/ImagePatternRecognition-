# ImagePatternRecognition-

Reconocimiento automático de placas vehiculares usando procesamiento de imágenes y OCR.

## Características

- Descarga y gestión de datasets de Kaggle.
- Procesamiento de imágenes con OpenCV.
- Detección y extracción de placas usando anotaciones.
- Lectura de texto en placas con Tesseract OCR.
- Ejemplos ejecutables en notebooks.

## Instalación

Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
sudo apt-get install tesseract-ocr libtesseract-dev
```

## Uso rápido

Ejecuta el pipeline básico en un notebook o script:

```python
from src.ocr_plate import read_plate

image_path = 'data/images/Cars0.png'
annotation_path = 'data/annotations/Cars0.xml'
text, plate_img = read_plate(image_path, annotation_path)
print("Texto detectado:", text)
```

## Estructura del proyecto

- `data/`: Imágenes y anotaciones.
- `notebooks/`: Ejemplos y experimentos.
- `src/`: Código fuente modular.

## Créditos

Dataset: [Car Plate Detection (Kaggle)](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection)
