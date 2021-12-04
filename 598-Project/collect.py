""" Comp598 Final Project
    data collection
    Hanzhi Z
"""
import sys
import tweepy
import datetime
import pandas as pd

today = datetime.date.today()

consumer_key = ['cduDckJL1S93EH37fOObVP809']
consumer_secret = ['uKAUae1c8iHISMJuZdk3oMICOlMnUVgpQadee6WJK5Mwfe1g1y']
# bearer_token = 'AAAAAAAAAAAAAAAAAAAAACgrVwEAAAAAknkrQU2Br%2FPoi%2FARdB550Wc0x7E%3DDyg7333SOTN8ZdwJvpP45hIAB74HyJ4dt67blo7CPmu8VaqYTq'
access_token = ['1341404696825786373-pAXIoJ9OTHVEGlsjhxB1uwmIuJNbof']
access_token_secret = ['Cm4gxGqWVCRdEovQphF60IGjxB2eYYIyI4RfHRGh83inw']

# approved COVID-19 vaccine:
# https://www.canada.ca/en/health-canada/services/drugs-health-products/covid19-industry/drugs-vaccines-treatments/vaccines.html

# need 1000+ posts
# COVID, vaccination, name-brand COVID vaccine

kw_cov = 'covid OR SARS-CoV-2 OR coronavirus '
kw_vac = 'OR vaccination OR Moderna OR Pfizer OR AstraZeneca OR (Janssen AND vaccine) '
kw_tag = 'OR #COVID OR #VACCINATION'


def t_auth(i):
    auth = tweepy.OAuthHandler(consumer_key[i], consumer_secret[i])
    auth.set_access_token(access_token[i], access_token_secret[i])
    api = tweepy.API(auth)

    return api


def collect(api, until_date, out_name):
    tweets_list = tweepy.Cursor(api.search_tweets,
                                q=kw_cov + kw_vac + kw_tag + '-filter:retweets',
                                tweet_mode='extended',
                                until=until_date,
                                lang='en').items(500)

    output = []
    for tweet in tweets_list:
        time, id, text, favorite_count = tweet._json['created_at'], tweet._json['id'], tweet._json['full_text'], \
                                         tweet._json['favorite_count']

        line = {'time': time, 'id': id, 'like': favorite_count, 'text': text.replace("\n", " ")}
        output.append(line)

    df = pd.DataFrame(output)
    df.to_csv(out_name)


if __name__ == "__main__":
    api = t_auth(0)

    collect(api, "2021-11-12", './output_1.csv')
    collect(api, "2021-11-13", './output_2.csv')
    collect(api, "2021-11-14", './output_3.csv')

