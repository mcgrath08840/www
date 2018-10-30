import requests
from flask import Flask, render_template, session, redirect, request, url_for, g
from twitter_utils import get_request_token, get_oauth_verifier_url, get_access_token, consumer
from user import User
from database import Database
import oauth2

app = Flask(__name__)
app.secret_key = '1234'    # required to use session Key

Database.initialise(user='postgres', password='odin1', database='learning', host='localhost')

# Load a user
@app.before_request
def load_user():
    if 'screen_name' in session:
        g.user = User.load_from_db_by_screen_name(session['screen_name'])  #'g' has to be imported from Flask
        # g variable doesn't die off when exit method.  Globally available.


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/login/twitter')
def twitter_login():
    if 'session_name' in session:   # check to see if user already logged in.
        return redirect(url_for('profile'))    # redirect to profile if logged in.
    request_token = get_request_token()
    session['request_token'] = request_token    # creates a cookie to remember variable.

    return redirect(get_oauth_verifier_url(request_token))

@app.route('/logout')   # Logout and clear session variable for security
def logout():
    session.clear()
    return redirect(url_for('homepage'))


@app.route('/auth/twitter')  # http://127.0.0.1:4996/auth/twitter?oauth_verifier=123456
def twitter_auth():
    oauth_verifier = request.args.get('oauth_verifier')
    access_token = get_access_token(session['request_token'], oauth_verifier)

    user = User.load_from_db_by_screen_name(access_token['screen_name'])
    if not user:
        user = User(access_token['screen_name'], access_token['oauth_token'],
                    access_token['oauth_token_secret'], None)
        user.save_to_db()

    session['screen_name'] = user.screen_name

    return redirect(url_for('profile'))   # Flask redirect to profile method below.

@app.route('/profile')
def profile():
    return render_template('profile.html', user=g.user) # use globale variable 'g' from Flask

@app.route('/search')
def search():
    #Require dynamic query
    query = request.args.get('q')

    # uses g.user to call twitter_request and passes url
    tweets = g.user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q={}'.format(query))

    # Uses list comprehension to get only the text elements from tweets info
    tweet_texts = [{'tweet': tweet['text'], 'label': 'neutral' } for tweet in tweets['statuses']]


    # Get sentiment
    for tweet in tweet_texts:
        r = requests.post('http://text-processing.com/api/sentiment/', data={'text': 'the tweet itself'})
        json_response = r.json()
        label = json_response['label']
        tweet['label'] = label

    # returns tweet text elements to the search.html page for display
    return render_template('search.html', content=tweet_texts)


app.run(port=4996, debug=True)  # debug is easier way.

