import json
import boto3
from datetime import datetime


def bajarArchivo():
    s3 = boto3.resource('s3')
    bucket = "biproyecto"
    file = "tweets/CD.json"

    content_object = s3.Object(bucket, file)

    file_content = content_object.get()['Body'].read().decode('utf-8')

    json_content = json.loads(file_content)
    # x = json_content[1]

    list = []
    list.append(json_content[0])
    dateApi = json_content[0]
    for i in range(len(json_content)):
        if i != 0:
            x = json_content[i]
            dic = {'id': x.get("id"), 'created_at': x.get("created_at"), 'text': x.get("text"), 'DateApi': dateApi,
                   'DateDL': str(datetime.today())}
            list.append(dic)
    print(list[1])

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(bajarArchivo())
    }
