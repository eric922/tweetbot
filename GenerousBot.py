import tweepy
import time

auth = tweepy.OAuthHandler("65uqamTabXPowkwWVexyXTazg", "z7GdTbhVAIArn3rN8cEgGCvQcaQ3D8GDwpkqRTSbjjP11jk6IM")
auth.set_access_token("248963399-oRtIEJD7xZOveMMiYE8FWJIbcdJumeOXPtPN7alf",
                      "E9yhicBpnnifbUuAH185tVfLn1dFK0qi5GVg3VQQ6dIx5")

api = tweepy.API(auth)

user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(3)


# Generous Bot

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    follower.follow()
