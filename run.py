import requests
import tweepy
from time import sleep
auth = tweepy.OAuthHandler('PlaceAPIKeyHere', 'PlaceAPISecretHere')
auth.set_access_token('PlaceAccessTokenHere', 'PlaceAccessTokenSecretHere')


interval = 60   # <-- Change to the amount of seconds between each check


#----------------------------------------------------------------



loop = True
count = 1

#-------------------

response = requests.get('http://gtfr5gtf5er4.herokuapp.com/cameracafeV2/habsite.php')
aes = response.text

#-------------------

while loop == True:
         response = requests.get('http://gtfr5gtf5er4.herokuapp.com/cameracafeV2/habsite.php')
         aesloop = response.text
         print("Comprobando si habsite tiene nuevas noticias de habbo: " ,count)
         count = count + 1
         sleep(interval)

         if aes != aesloop:
                  print("Nuevas Noticias...")
                  try:
                           url = "http://gtfr5gtf5er4.herokuapp.com/cameracafeV2/noticias.php"
                           response = requests.get(url)
                           Video = response.json()["Video"]
                           

                           api = tweepy.API(auth)
                           api.update_status(""+Video+"\n\n\n\n")
                           loop = False
                           print("Habsite tienes nuevas noticias de habbo, twiteando... Por favor, vuelva a ejecutar el programa.")
                  except:
                           print("ERROR: Tweepy module is not working, aes key has changed but not tweeted! Please re-run the program.") # Error line
                           loop = False

