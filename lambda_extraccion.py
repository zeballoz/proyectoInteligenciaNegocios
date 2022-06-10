import tweepy
import json
import numpy as np
import boto3
import pandas as pd


def autentificacion():
    # Cadenas de autentificacion
    consumer_key = "818PH4Ji0VAne2jl0NEQJqo1n"
    consumer_secret = "PpiAFaKzNNoeMiV7h5XOY8OtVW27KfkiR5HozocQrHbP122cMt"

    access_token = "175881569-1WpRDk3NduAHjjjXoiOIvLGwNQNdgZB7j5LEGS23"
    access_token_secret = "lXNAEJqX6ARs5UuDxAmfacLbO7l0piEfm6GQWtKGPOhQC"

    # Metodo que nos permite autentificarnos con el api
    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )

    api = tweepy.API(auth)

    return api



def extraccionDatos():
    api = autentificacion()
    dataFinal = api.search_tweets('elecciones')

    for i in range(1):
        # Carga de Archivos
        dataRecoleccion = api.search_tweets('elecciones')
        dataFinal = np.concatenate((dataFinal, dataRecoleccion))
    return dataFinal




def cargaData():
    dataFinal = extraccionDatos()
    #Se crea una lista y de esta forma transformarla a .json
    lista = []

    for i in range(len(dataFinal)):
        lista.append(dataFinal[i]._json)

    jsonFinal = json.dumps(lista)

    s3 = boto3.client('s3')
    bucket = 'biproyecto'
    objeto = 'tweets/'

    fileName = objeto + 'CID-12223' + '.json'

    s3.put_object(Bucket=bucket, Key=fileName, Body=jsonFinal)



def lambda_handler(event, context):
    cargaData()
    return {
        'statusCode': 200,
        'body': json.dumps('se ha realizado la extraccion correctamente !!')
    }