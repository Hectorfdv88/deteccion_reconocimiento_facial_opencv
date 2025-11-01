# Detección y Reconocimiento Facial con OpenCV

Proyecto de reconocimiento facial utilizando OpenCV que implementa detección y reconocimiento de rostros usando EigenFaces. El sistema puede entrenarse con imágenes de diferentes personas y reconocerlas en imágenes estáticas y videos en tiempo real.

## 📋 Descripción

Este proyecto utiliza algoritmos de visión por computadora para:
- **Detección facial**: Identifica rostros en imágenes y videos usando Haarcascade
- **Reconocimiento facial**: Clasifica rostros conocidos usando EigenFaces
- **Entrenamiento**: Procesa imágenes de referencia para crear un modelo de reconocimiento
- **Captura de datos**: Extrae rostros de videos para construir bases de datos de entrenamiento

## 🗂️ Estructura del Proyecto

```
Reco/
├── rostros/                  # Base de datos de rostros para entrenamiento
│   ├── duque/                # ~100 imágenes del rostro de Duque
│   └── obama/                # ~100 imágenes del rostro de Obama
├── video/                    # Videos para pruebas y captura de datos
│   ├── duque.mp4
│   ├── duque_test.mp4
│   ├── obama.mp4
│   ├── obama_test.mp4
│   └── obama_test2.mp4
├── entrenamiento.py          # Script para entrenar el modelo EigenFaces
├── main.py                   # Detección facial en imagen estática
├── VideoRec.py               # Captura de rostros desde video
├── VideoTest.py              # Reconocimiento facial en tiempo real
├── mr_bean.jpg               # Imagen de prueba
├── eigenface.xml             # Modelo entrenado (generado)
└── README.md                 # Este archivo
```

## 🔧 Requisitos

- Python 3.x
- OpenCV (`cv2`)
- NumPy

### Instalación

```bash
pip install opencv-python numpy
```

## 📝 Uso

### 1. Captura de Rostros desde Video (`VideoRec.py`)

Extrae rostros de un video para crear tu base de datos de entrenamiento.

**Instrucciones:**
- Ejecuta el script cargando un video
- Presiona `c` cada vez que detecte un rostro que quieras capturar
- Los rostros se guardarán automáticamente en `rostros/[persona]/`

```bash
python VideoRec.py
```

**Características:**
- Detecta rostros con Haarcascade
- Permite captura manual de frames con la tecla `c`
- Guarda imágenes de 120x120 pixels mínimo
- Muestra contador de rostros capturados

### 2. Entrenamiento del Modelo (`entrenamiento.py`)

Entrena el modelo EigenFaces con las imágenes de la base de datos.

```bash
python entrenamiento.py
```

**Proceso:**
1. Lee todas las imágenes de `rostros/duque/` y `rostros/obama/`
2. Convierte a escala de grises y redimensiona a 150x150
3. Asigna etiquetas: Duque=0, Obama=1
4. Entrena el modelo EigenFaceRecognizer
5. Guarda el modelo en `eigenface.xml`

### 3. Detección Facial Estática (`main.py`)

Prueba la detección de rostros en una imagen estática.

```bash
python main.py
```

**Características:**
- Detecta rostros en `mr_bean.jpg`
- Dibuja rectángulos azules alrededor de las caras detectadas
- Parámetros: `scaleFactor=1.3`, `minNeighbors=5`, rango 30x30 a 500x500

### 4. Reconocimiento en Video (`VideoTest.py`)

Reconoce personas conocidas en un video en tiempo real.

```bash
python VideoTest.py
```

**Funcionalidad:**
- Carga el modelo entrenado desde `eigenface.xml`
- Detecta rostros en cada frame del video
- Identifica si es una persona conocida o desconocida
- Muestra el nombre o "Desconocido" sobre cada rostro
- Umbral de confianza: <3000 para reconocimiento válido

**Salir:** Presiona `ESC`

## 🤖 Algoritmos Utilizados

### Haarcascade
- Modelo pre-entrenado para detección de rostros frontales
- Ventana deslizante con pirámide de escalas
- Alto rendimiento y bajo costo computacional

### EigenFaces
- Método estadístico de reconocimiento facial
- Análisis de Componentes Principales (PCA)
- Genera vectores característicos de rostros
- Compatible con imágenes de baja resolución (150x150)

## ⚙️ Parámetros Configurables

### Detección de Rostros
```python
detectMultiScale(gray, 
    scaleFactor=1.3,      # Factor de escalado
    minNeighbors=5-10,    # Vecinos mínimos para confirmar detección
    minSize=(30-120, 30-120),  # Tamaño mínimo del rostro
    maxSize=(500-600, 500-600) # Tamaño máximo del rostro
)
```

### Reconocimiento
```python
predict[1] < 3000  # Umbral de confianza para reconocimiento válido
```

## 📊 Datos de Entrenamiento

- **Duque**: ~100 imágenes
- **Obama**: ~100 imágenes
- **Formato**: 150x150 píxeles, escala de grises
- **Fuente**: Frames extraídos de videos


## 📄 Licencia

Este proyecto es de uso educativo.
