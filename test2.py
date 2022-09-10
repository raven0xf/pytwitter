import pytwitter
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
API_SECRET="XXXXXXXXXXXXXXXXXXXXXXXXXX"


# Authorization using user context
pytwitter.ucontext(API_KEY, API_SECRET)

# Look up a user by name, using specific fields or parameters
# created_at, description, entities, id, location, name,
# pinned_tweet_id, profile_image_url, protected,
# public_metrics, url, username, verified, and withheld

pytwitter.lookUpUserByName("USERNAME", "PARAMETER")
pytwitter.unretweet(XXXXXXX, XXXXXXX)

print('[*] Retweet successfully undone')
