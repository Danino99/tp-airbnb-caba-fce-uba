# TP Grupal · Dinámica de Virales en YouTube

**Trabajo Práctico Grupal · Tecnicatura en Gestión y Análisis de Datos** Facultad de Ciencias Económicas · UBA · 1er Cuatrimestre 2026

## Pregunta de investigación
¿Cómo evoluciona la popularidad de los videos virales de YouTube en el tiempo, y qué características del canal, contenido o región se asocian con curvas de crecimiento más explosivas o vidas más prolongadas en el ranking?

## Integrantes
- Daniel Quezada · Registro N°921316 · GitHub: [@Danino99](https://github.com/Danino99)
- Matías Mallón · Registro N°921268 · GitHub: [@matimallon1](https://github.com/matimallon1)

## Dataset
**Trending YouTube Video Statistics (113 Countries)** obtenido de [Kaggle](https://www.kaggle.com/datasets/asaniczka/trending-youtube-videos-113-countries).

*Nota de Preprocesamiento:* El archivo original de 7.3 GB fue procesado mediante Python y reducido a un subconjunto de 44.58 MB (`youtube_filtered.csv` con 266,022 filas) aplicando los siguientes parámetros de ingesta:
- **Filtro geográfico (6 países):** AR, US, BR, MX, ES, GB.
- **Filtro temporal:** `snapshot_date` >= `2024-01-01` (hasta junio de 2026).
- **Optimización de dimensionalidad:** Eliminación de *features* no estructurados o de alto peso computacional (`description`, `thumbnail_url`, `video_tags`, `kind`).

## Estructura del Repositorio
- `data/` — dataset filtrado y preprocesado.
- `notebook/` — notebook de análisis en Python (Colab exportado a `.ipynb`).
- `informe/` — informe académico en formato PDF.
- `presentacion/` — slides y materiales audiovisuales para la exposición.
- `figuras/` — gráficos exportados desde el entorno de análisis.

## Concepto de la materia aplicado
Cálculo de derivadas e integrales numéricas sobre series temporales para modelar la velocidad de crecimiento (aceleración de vistas y métricas de *engagement*) y el alcance total (área bajo la curva) de cada contenido de video.

## Entrega
- **Cierre de entrega:** Jueves 11 de junio de 2026, 19:00 h.
- **Defensa oral:** Viernes 12 de junio.
