#!/usr/bin/env python3
import requests

def main():
  mytoken = '6806eeb6715f457e4480d0736665ea32f9f2908c52315ccf'
  myapi = "https://fonoapi.freshpixl.com/v1/getlatest"
  mybuiltapi = myapi + "?token=" + mytoken

  ## translate our JSON response to a series of Python lists and dictionaries
  myjson = requests.get(mybuiltapi).json()

  ## Display a list of what inside our JSON
  for x in myjson:
    print(x)

if __name__ == '__main__':
  main()
