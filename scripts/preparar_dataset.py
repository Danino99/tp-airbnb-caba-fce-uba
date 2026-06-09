"""
Preprocesamiento del dataset original de Trending YouTube Video Statistics (113 Countries).

Este script reduce el archivo original (7.3 GB descomprimido) a un subconjunto
manejable de 6 países y desde 2024-01-01, eliminando columnas de texto pesadas.

Uso:
    1. Descargar el dataset original de Kaggle:
       https://www.kaggle.com/datasets/asaniczka/trending-youtube-videos-113-countries
    2. Ajustar la variable RUTA_ORIGINAL a la ubicación local del archivo.
    3. Ejecutar: python scripts/preparar_dataset.py
    4. El archivo filtrado se guarda en data/youtube_filtered.csv.

Resultado esperado: ~266.000 filas, ~45 MB.
"""
import os
import pandas as pd

# ---- AJUSTAR SEGÚN LA UBICACIÓN LOCAL DEL ARCHIVO ORIGINAL ----
RUTA_ORIGINAL = '/mnt/c/Users/danie/Downloads/archive/trending_yt_videos_113_countries.csv'
RUTA_SALIDA = 'data/youtube_filtered.csv'

# Filtros del proyecto
PAISES = ['AR', 'US', 'BR', 'MX', 'ES', 'GB']
FECHA_DESDE = '2024-01-01'
COLUMNAS_ELIMINAR = ['description', 'thumbnail_url', 'video_tags', 'kind']

# Asegurar que existe la carpeta de salida
os.makedirs(os.path.dirname(RUTA_SALIDA), exist_ok=True)

# Si ya existe el archivo de salida previo, eliminarlo para empezar limpio
if os.path.exists(RUTA_SALIDA):
    os.remove(RUTA_SALIDA)

print(f"Preprocesando {RUTA_ORIGINAL} en chunks...")
chunksize = 1_000_000
total_filas = 0
primer_chunk = True

for i, chunk in enumerate(pd.read_csv(RUTA_ORIGINAL, chunksize=chunksize, low_memory=False)):
    # Filtros aplicados en cada chunk
    chunk = chunk[chunk['country'].isin(PAISES)]
    chunk = chunk[chunk['snapshot_date'] >= FECHA_DESDE]
    cols_a_eliminar = [c for c in COLUMNAS_ELIMINAR if c in chunk.columns]
    chunk = chunk.drop(columns=cols_a_eliminar)

    if len(chunk) > 0:
        total_filas += len(chunk)
        chunk.to_csv(RUTA_SALIDA, mode='a', index=False, header=primer_chunk)
        primer_chunk = False

    print(f"  Chunk {i + 1} procesado, {total_filas:,} filas acumuladas")

# Reporte final
print("\nPreprocesamiento finalizado. Generando reporte...")

df_final = pd.read_csv(RUTA_SALIDA, low_memory=False)
tamano_mb = os.path.getsize(RUTA_SALIDA) / (1024 * 1024)

print("\n=== REPORTE ===")
print(f"Filas finales: {len(df_final):,}")
print(f"Tamaño del archivo: {tamano_mb:.2f} MB")
print(f"Rango de fechas: {df_final['snapshot_date'].min()} a {df_final['snapshot_date'].max()}")
print(f"Videos únicos: {df_final['video_id'].nunique():,}")
print("Conteo por país:")
for pais, conteo in df_final['country'].value_counts().items():
    print(f"  {pais}: {conteo:,}")