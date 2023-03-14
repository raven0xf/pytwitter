# twPy v 0.1
A simple but extremely reliable Python library for accessing the Twitter API.
twPy prioritizes swiftness and simplicity over everything else.

This is still a WiP project.
For now, it's not on PyPi

## Proof of concept

```
from twPy import *

API_KEY = "XXXXXX"
API_SECRET = "XXXXXXXXXXXXXXXX"

tw.auth(API_KEY, API_SECRET)
tw.createTweet("Hello world!")
```

## Additional information

As of now, the authorization process is not that speedy, but this version is still in alpha phase and soon will have very serious and useful changes with its simplicity intact.

This is what it currently looks like: 

![alt text](https://github.com/jasonmichael13/pytwitter/blob/main/alpha-auth.png?raw=true)


## Forthcoming features

I compiled a list of features that I would like to add to this library:

* User login
* Searching for specific keywords
* Follow and unfollow user(s)
* Fetch followers of user(s)

There is more to come.
