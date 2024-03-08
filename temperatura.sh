#!/bin/bash

#**********************
# temperatura
# obtiene la temperatura de cpu y gpu genera una cadena con el siguiente formato y la deja en /$SCRATCH_DIR/$OUTPUT_FILE
#   formato de salida: 2024-03-08 09:00:01 - CPU Temperature: +47.0°C°C, GPU Temperature: 54 52°C   
#
#
#  v2024.03.06 tested
#**********************



# Directorio para almacenar los datos
SCRATCH_DIR="/tmp"
OUTPUT_FILE="temperaturas.log"


# Obtener la temperatura de la CPU --- depende de lm-sensors
CPU_TEMP=$(sensors | grep 'Tdie' | awk '{print $2}')

# Obtener la temperatura de la GPU --- depende de nvidia-smi
GPU_TEMP=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits)


TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")



LOG_ENTRY="$TIMESTAMP - CPU Temperature: $CPU_TEMP°C, GPU Temperature: $GPU_TEMP°C"
echo $LOG_ENTRY >> "$SCRATCH_DIR/$OUTPUT_FILE"