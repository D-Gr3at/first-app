# A package contains all the files you need for a module. 
# Modules are Python code libraries you can include in your project.

import camelcase as cs
import requests as req

if __name__ == '__main__':
    print(cs.CamelCase)

    response = req.get('https://xkcd.com/1906/')

    print(response.text)


    # https - HyperText Transfer Protocol Secure
    # http - HyperText Transfer Protocol
