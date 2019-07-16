#!/usr/bin/env python3

#LOOKUPAPI ="https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=95630&date=2019-07-16&distance=25&API_KEY=B28E6CE5-2B73-4A29-B6A4-D6F73E49EE9C" 

zip_code = input("Enter your zipcode: ")
print(zip_code)
LOOKUPAPI ="https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+zip_code+"&date=2019-07-16&distance=25&API_KEY=B28E6CE5-2B73-4A29-B6A4-D6F73E49EE9C" 
print(LOOKUPAPI)
# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    ## set up screen
    print("Weather Forecast")
    print("----------------")

    # display the JSON we were returned as Pythonic datastructures
# loop across the list returned to us
    for x in r.json():
        print(x.get("DateForecast"))
        print("----------")
        print(x.get("Discussion"))

main()
