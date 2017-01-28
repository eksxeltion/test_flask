
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

auth = Oauth1Authenticator(
    consumer_key=os.environ['YELP_CONSUMER_KEY'],
    consumer_secret=os.environ['YELP_CONSUMER_SECRET'],
    token=os.environ['YELP_TOKEN'],
    token_secret=os.environ['YELP_TOKEN_SECRET']
)

#term = input("What food are you looking for?")
#location = input("Where are you searching in?")


def get_places(term, location):
    client = Client(auth)
    params = {
        'term': term,
        'lang': 'en',
        'sort': 2
    }
    response = client.search(location, **params)

    businesses = []

    for business in response.businesses:
        #print("{}, {} rating, call {}".format(business.name, business.rating, business.phone))
        businesses.append(
            {
                "name" : business.name,
                "rating" : business.rating,
                "phone" : business.phone
            }
        )
    return businesses

def get_top_places(term, location, top):
    client = Client(auth)
    params = {
        'term': term,
        'lang': 'en',
        'sort': 2
    }
    response = client.search(location, **params)

    businesses = []

    for n in range(0, top):
        #print("{}, {} rating, call {}".format(business.name, business.rating, business.phone))
        business = response.businesses[n]
        businesses.append(
            {
                "name" : business.name,
                "rating" : business.rating,
                "phone" : business.phone,
                "rank" : n+1
            }
        )
    return businesses

# businesses = get_food(term, location)

# for business in businesses:
#     print(business['name'])
#     print(business['rating'])
#     print(business['phone'])
