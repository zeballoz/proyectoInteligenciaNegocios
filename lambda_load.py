import json
import boto3
from datetime import datetime
import psycopg2
from datetime import datetime
import random


def cargarArchivo():
    s3 = boto3.resource('s3')
    bucket = "biproyecto"
    file = "tweets/Transformados.json"
    content_object = s3.Object(bucket, file)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    return json_content


def cargaData():
    try:
        conexion = psycopg2.connect(

            host='rdsbi.cfphb80ue0u6.us-east-1.rds.amazonaws.com',
            user='postgres',
            password='12345678',
            database='proyectoBi'
        )

        cursor = conexion.cursor()

        dataFinal = cargarArchivo()

        for i in range(len(dataFinal)):

            if i != 0:
                sql = "insert into tweet(id_tweet,fecha_creacion,texto,fecha_consulta_api, fecha_data_lake, fecha_data_warehouse,id_usuario) values (%s,%s,%s,%s,%s,%s,%s)"
                tweet = (
                str(random.randint(0, 100000)), str(dataFinal[i].get("created_at")), str(dataFinal[i].get("text")),
                str(dataFinal[i].get("DateApi")), str(dataFinal[i].get("DateDL")), str(datetime.today()),
                str(dataFinal[i].get("id")))
                cursor.execute(sql, tweet)
                conexion.commit()

        print("Carga de datos finalizada !!")

    except Exception as ex:
        print(ex)


def lambda_handler(event, context):
    cargaData()

    return {
        'statusCode': 200,
        'body': json.dumps('Carga de datos finalizada, proceso acabado !!')
    }