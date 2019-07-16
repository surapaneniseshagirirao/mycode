#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

LOOKUPAPI = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=95630&date=2019-07-16&distance=25&API_KEY=B28E6CE5-2B73-4A29-B6A4-D6F73E49EE9C"

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    # display the methods available to our new object
    print( dir(r) )

main()
