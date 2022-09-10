from requests_oauthlib import OAuth1Session
import json

global url
url = "https://api.twitter.com/"


# Auth class, including different oauth options. Edit: The only authentication method implemented RN is OAuth1 user context.
def ucontext(consumer_key, API_SECRET): # Authentication using user context (API key/secret or consumer key/secret)
    # DONT BLAME ME FOR THE SHITTY TERMINILOGY/

    # Important global variables so they could be imported in other files. tl;dr: I suck at coding.
    global con_key
    global oauth
    global api_sec


    con_key = consumer_key
    api_sec = API_SECRET
    request_token_url = url + "oauth/request_token"
    oauth = OAuth1Session(con_key, api_sec)
    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError as e:
        print("[!] Error: ", e)
    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("[*] OAuth token: %s" % resource_owner_key)

    base_authorization_url =  url + "oauth/authorize" # This authorization URL will redirect you to your callback URL to acquire the verifier pin code
    authorization_url = oauth.authorization_url(base_authorization_url)
    print("Go here for authorization: %s" % authorization_url)
    verifier = input("PIN/verifier : ")
    access_token_url = url + "oauth/access_token"

    oauth = OAuth1Session( # Authorization with the verifier PIN code to receive the access token for further authorization
        con_key,
        client_secret=api_sec,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

        # Make the request

        # Final authorization using the access token, consumer key and consumer secret
    oauth = OAuth1Session(
        con_key,
        client_secret=api_sec,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
)
