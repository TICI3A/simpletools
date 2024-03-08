from datetime import datetime
from socket import gethostname
from elasticsearch import Elasticsearch
import re


# Configuración de Elasticsearch
es = Elasticsearch(['http://host:9200'])
index_name = 'temperatura_logs'
log_file_path = '/tmp/temperaturas.log'
host_name = gethostname()


# Patrón para extraer información de los logs
log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - CPU Temperature: ([+\-]?\d+\.\d+)°C.*?GPU Temperature: ([+\-]?\d+)')


# Leer el archivo de logs y enviar cada entrada a Elasticsearch
with open(log_file_path, 'r') as file:
     for line in file:
         match = log_pattern.search(line)
         if match:
             timestamp = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
             cpu_temperature = float(match.group(2))
             gpu_temperature = float(match.group(3))

             # Crear un ID único usando el nombre del host y el timestamp
             document_id = f"{host_name}_{timestamp.strftime('%Y%m%d%H%M%S')}"

             
             document = {
                 'timestamp': timestamp,
                 'cpu_temperature': cpu_temperature,
                 'gpu_temperature': gpu_temperature
             }

             # Enviar el documento
             es.index(index=index_name, id=document_id, body=document)