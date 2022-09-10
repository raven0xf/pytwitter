import pytwitter.twauth
from requests_oauthlib import OAuth1Session
from .parse import *

url = pytwitter.twauth.url

# Lots of repetitions because of minor differences.
# If there's any better way to do it, please contact me

def createTweet(twt):

    payload = {"text": f"{twt}"}

    response = pytwitter.twauth.oauth.post(url + "2/tweets",json=payload)
    json_dump(response, response.status_code)


def deleteTweetById(id):

    response = pytwitter.twauth.oauth.delete( url + "/2/tweets/{}".format(id))

    json_dump(response, response.status_code)


def lookUpUserByName(usernames, fields): # in the first arg, you input the target username. You can also use some of the many fields:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld

    params = {"usernames":f"{usernames}","user.fields": fields}

    response = pytwitter.twauth.oauth.get(
        url + "2/users/by", params=params
        )
    json_dump(response, response.status_code)

def blockUserById(id, idtoblock):
    payload = {'target_user_id':f'{idtoblock}'}

    response = pytwitter.twauth.oauth.post(
    url + "2/users/{}/blocking".format(id), json=payload
        )

    json_dump(response, response.status_code)

def lookUpTweetById(ids, fields):
    params = {"ids":f"{ids}", "tweet.fields":f"{fields}"}
    response = pytwitter.twauth.oauth.get(url + "2/tweets", params=params)

    json_dump(response, response.status_code)

# The user ID must be the ID of the authenticated user.
# The tweet ID belongs to the one the user would retweet
def retweet(user_id, tweet_id):
    rtwt = {"tweet_id":f"{tweet_id}"}

    response = pytwitter.twauth.oauth.post(url + "2/users/{}/retweets".format(user_id), json=rtwt)

    json_dump(response, response.status_code)

# The user ID must be the ID of the authenticated users
#
def unretweet(user_id, tweet_id):

    response = pytwitter.twauth.oauth.delete(url + "2/users/{}/retweets/{}".format(user_id, tweet_id))

    json_dump(response, response.status_code)
