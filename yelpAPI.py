#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:42:05 2016

@author: leena
"""

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json


# read API keys
with open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

client = Client(auth)

params = {
    'term': 'food',
    'location': 'Baltimore'
}

response = client.search(**params)

print(response.businesses[1].location.neighborhoods)
