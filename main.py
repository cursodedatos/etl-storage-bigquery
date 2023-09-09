# -*- coding: utf-8 -*-
import functions_framework
from google.cloud import bigquery
from google.cloud import storage
import csv
from io import StringIO
import json
import logging, traceback
import datetime
import sys

@functions_framework.http
def main(request):
    try:
        # Extract from Storage
        storage_client = storage.Client()
        buket_name = 'curso_datos_bucket'
        bucket = storage_client.bucket(buket_name)
        blob = bucket.blob('bank.csv')
        file = blob.download_as_text()
        f = StringIO(file)
        data_csv = csv.reader(f,delimiter=';')
        line_count = 0

        rows_to_insert = []
        # Transform Data
        now = datetime.datetime.now()
        for row in data_csv:
            line_count += 1
            if line_count == 1:
                pass
            else:            
                data_bigquery = {
                    "age" : row[0],
                    "job" : row[1],
                    "balance" : row[5]
                }
            rows_to_insert.append(data_bigquery)
        # Load in Big Query
        table_id = "curso-datos-398001.cursodatos.bank"
        client_bigquery = bigquery.Client()
        errors = client_bigquery.insert_rows_json(table_id, rows_to_insert)
        print(errors)
        return json.dumps({"success": True, "message": str(errors) }),200
    except:
        logging.warning("Error in main function")
        logging.warning(sys.exc_info()[0])
        logging.warning(traceback.format_exc())
        return json.dumps({"success": False, "message": "Error Response" }),500



