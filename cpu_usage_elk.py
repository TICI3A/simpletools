#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from datetime import datetime
from elasticsearch import Elasticsearch

# Configuración de Elasticsearch
es = Elasticsearch(['http://host:9200'])
index_name = 'cpu_usage'

def obtener_valores():

    hostname = subprocess.check_output("hostname", shell=True, text=True).strip()
    timestamp = datetime.utcnow()

    command_output = subprocess.check_output("condor_status -compact | grep -v nv | grep -v worker | grep -v a100", shell=True, text=True)
    lines = command_output.split('\n')

    total_cpus = 0
    free_cpus = 0

    # Ignorar la primera línea que contiene la cabecera
    for line in lines[1:]:
        columns = line.split()

        # Asegurarse de que hay suficientes columnas
        if len(columns) >= 9:
            # Obtener el número total de CPUs y CPUs libres
            total_cpus += int(columns[3])
            free_cpus += int(columns[5])

    # Calcular el porcentaje de utilización de las CPUs
    utilization_percentage = int(((total_cpus - free_cpus) / total_cpus) * 100) if total_cpus > 0 else 0

    # Lo devolvemos ya como documento
    return {
        'timestamp': timestamp,
        'hostname': hostname,
        'total_cpus': total_cpus,
        'free_cpus': free_cpus,
        'utilization_percentage': utilization_percentage
    }

def enviar_a_elasticsearch(document):
    # Crear un documento para Elasticsearch
    document_id = f"{document['hostname']}_{document['timestamp'].strftime('%Y%m%d%H%M%S')}"

    # Enviar el documento a Elasticsearch con el ID personalizado
    es.index(index=index_name, id=document_id, document=document)


# Ejecución
documento = obtener_valores()
enviar_a_elasticsearch(documento)
