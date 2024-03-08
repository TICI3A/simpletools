#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from datetime import datetime, timedelta

# Configuración de Elasticsearch
es = Elasticsearch(['http://host:9200'])
index_name = 'temperatura_logs'

# tomaremos los últimos 30 días
end_time = datetime.utcnow()
start_time = end_time - timedelta(days=30)

query = {
    "query": {
        "range": {
            "timestamp": {
                "gte": start_time.isoformat(),
                "lte": end_time.isoformat()
            }
        }
    }
}

# consulta
result = es.search(index=index_name, body=query)

# Procesar los resultados y calcular la media de las temperaturas
total_cpu_temperature = 0
total_gpu_temperature = 0
num_documents = len(result['hits']['hits'])

for hit in result['hits']['hits']:
    total_cpu_temperature += hit['_source']['cpu_temperature']
    total_gpu_temperature += hit['_source']['gpu_temperature']

# Calcular la media
average_cpu_temperature = total_cpu_temperature / num_documents if num_documents > 0 else 0
average_gpu_temperature = total_gpu_temperature / num_documents if num_documents > 0 else 0


# Cambiar el color según temperatura
if average_cpu_temperature < 50 and average_gpu_temperature < 60:
    color = '\033[92m'  # Verde
elif 50 <= average_cpu_temperature <= 55 and 60 <= average_gpu_temperature <= 65:
    color = '\033[93m'  # Amarillo
else:
    color = '\033[91m'  # Rojo

print(f"{color}Media de CPU Temperature en los últimos 30 días: {average_cpu_temperature:.2f}°C\033[0m")
print(f"{color}Media de GPU Temperature en los últimos 30 días: {average_gpu_temperature:.2f}°C\033[0m")
