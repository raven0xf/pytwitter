# pytwitter v 0.1
A simple but extremely reliable Python library for accessing the Twitter API.
Pytwitter prioritizes swiftness and simplicity over everything else.

This is still a WiP project.
For now, it's not on PyPi

## Proof of concept

```
from pytwitter import *

API_KEY = "XXXXXX"
API_SECRET = "XXXXXXXXXXXXXXXX"

tw.auth(API_KEY, API_SECRET)
tw.createTweet("Hello world!")
```

## Additional information

As of now, the authorization process is not that speedy, but this version is still in alpha phase and soon will have very serious and useful changes with its simplicity intact.

This is what it currently looks like: 

![alt text](https://github.com/jasonmichael13/pytwitter/alpha-auth.jpg?raw=true)


## Forthcoming features

I compiled this list of features that I would like to add to this library:

1- User login
2- Searching for specific keywords
3- Follow and unfollow user(s)
4- Fetch followers of user(s)

There is more to come.
