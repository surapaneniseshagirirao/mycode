#!/usr/bin/env python3
import urllib.request
import json
import webbrowser

## Define APOD 
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=PV1NrH9WhETSHNTEtdczM0g5Uo2YUTcRJrhaqkrS'    ## your key goes in place of DEMO_KEY

## Call the webservice
apodurlobj = urllib.request.urlopen(apodurl + mykey)

## read the file-like object
apodread = apodurlobj.read()

## decode JSON to Python data structure
decodeapod = json.loads(apodread.decode('utf-8'))

## display our Pythonic data
print("\n\nConverted Python data")
print(decodeapod)

## use Firefox to open the HTTPS URL
input('\nPress Enter to open NASA Picture of the Day in Firefox')
webbrowser.open(decodeapod['url'])
