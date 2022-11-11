import requests
import time

#api_url = "https://v2.jokeapi.dev/joke/Programming?type=single"

#response = requests.get(api_url)

#print(response) # This will print the response status (Ideally a 200 if everything went fine)

## Lets examine Response further
# print(dir(response))

## Use response.text
#print(response.text)
#print(type(response.text))

## Use response.json
#print(response.json()) # Note that 'json' is a method vs response.text (text is an 'attribute')
#print(type(response.json()))

## Not that we know that `response.json()` is a dictionary. We can fetch individuall elements as per our requirements
#o = response.json()
#print(o)
#print(f"Is Error : {o['error']}")
#print(f"Category : {o['category']}")
#print(f"Joke     : {o['joke']}")

## Lets make it a bit more interactive with 'two part' jokes
#api_url = "https://v2.jokeapi.dev/joke/Programming?type=twopart"

#o = requests.get(api_url).json() 
#print(o) # check the structure of the response
#len_setup = len(o["setup"])
#len_delivery = len(o["delivery"])
#print("-"*(len_setup if len_setup > len_delivery else len_delivery))
#print(o["setup"])
#time.sleep(3)
#print(o["delivery"])
#print("-"*(len_setup if len_setup > len_delivery else len_delivery))

## Let's try it with a 'normal' web page
o = requests.get("https://xkcd.com")
#print(o.text) # Note that the o.json() call will fail as the response is not a valid/well-formed JSON

## NEXT :: Simple Web scraper (of sorts) see - simple_scraper.py
