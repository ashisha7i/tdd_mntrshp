import requests

o = requests.get("https://xkcd.com")
#print(o.text) # Note that the o.json() call will fail as the response is not a valid/well-formed JSON

for line in o.text.split("\n"):
    if line.startswith("Permanent link to this comic: "):
        print(str(line)) # This should give you the direct link to the comic

## We can parse the string by hand, but then this is where 'beautiful soup' comes into picture
# pip3 install beautifulsoup4
