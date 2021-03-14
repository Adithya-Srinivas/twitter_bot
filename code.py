import tweepy
import time

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('','')

api = tweepy.API(auth)
user = api.me()


def limit_handle(cursor):                           # this is a limit handler in case there is an error 
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)
        except StopIteration:
            break


search_string = ''                                # a search string is keyword used to search and give likes using favorite
NumberOftweets = 10                               # no.of tweets to which likes given
public_tweets = api.home_timeline()
for tweet in limit_handle(tweepy.Cursor(api.search, search_string).items(NumberOftweets)):
    try:
        tweet.favorite()
        print("DONE!!!!!!!!!!!!!!!!!!!!")
    except tweepy.TweepError as e:
        print(e.reason)
