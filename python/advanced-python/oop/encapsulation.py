import oauth2
import urllib.parse as urlparse

class TwitterConsoleLogin:
    def __init__(self, consumer_key, consumer_secret):
        self.__consumer = oauth2.Consumer(consumer_key, consumer_secret)

    def perform_twitter_login(self):
        request_token = self.__get_request_token()
        verifier = self.__get_oauth_verifier(request_token)
        return self.__get_access_token(request_token, verifier)

    # To encapsulate methods put "__" in front of name. Can't call directly.
    def __get_request_token(self):

        client = oauth2.Client(self.__consumer)

        # use client to perform a request.
        response, content = client.request('https://api.twitter.com/oauth/request_token', 'POST')
        if response.status != 200:
            print("An error ocurred getting the request token from twitter!")

        return dict(urlparse.parse_qsl(content.decode('utf-8')))

    def __get_oauth_verifier(self, request_token):
        print("GO to the following site in your browser")
        print(self.__get_oauth_verifier_url(request_token))

        return input("What is the PIN?")

    def __get_oauth_verifier_url(self, request_token):
        return "{}?oauth_token={}".format('https://api.twitter.com/oauth/request_token', request_token['oauth_token'])

    def __get_access_token(self, request_token, oauth_verifier):
        token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
        token.set_verifier(oauth_verifier)
        client = oauth2.Client(self.__consumer, token)

        response, content = client.request('https://api.twitter.com/oauth/request_token', 'POST')
        return dict(urlparse.parse_qsl(content.decode('utf-8')))

twitter_login = TwitterConsoleLogin('my_key', 'my_secret')
twitter_login.perform_twitter_login()