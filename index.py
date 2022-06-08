
import tweepy
import json
import numpy as np

def pro():

   # Cadenas de autentificacion
   consumer_key = "818PH4Ji0VAne2jl0NEQJqo1n"
   consumer_secret = "PpiAFaKzNNoeMiV7h5XOY8OtVW27KfkiR5HozocQrHbP122cMt"

   access_token = "175881569-1WpRDk3NduAHjjjXoiOIvLGwNQNdgZB7j5LEGS23"
   access_token_secret = "lXNAEJqX6ARs5UuDxAmfacLbO7l0piEfm6GQWtKGPOhQC"


   #Metodo que nos permite autentificarnos con el api
   auth = tweepy.OAuth1UserHandler(
      consumer_key, consumer_secret, access_token, access_token_secret
   )

   api = tweepy.API(auth)

   dataFinal = api.search_tweets('elecciones')



   for i in range(50):
      #Carga de Archivos
      dataRecoleccion = api.search_tweets('elecciones')
      dataFinal = np.concatenate((dataFinal, dataRecoleccion))

   return len(dataFinal)

print(pro())