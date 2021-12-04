""" Comp598 Final Project
    data collection
    Hanzhi Z
"""
import sys
import tweepy
import datetime
import pandas as pd
import random
import time

today = datetime.date.today()

consumer_key = ['bmM4sJs9DRqUD342JvaXPqkJW']
consumer_secret = ['4pGFalnyTctieKqGctb9J1nzTwVmdD1cIwu9Z1ECh9aTWQ4HaW']
# bearer_token = 'AAAAAAAAAAAAAAAAAAAAACgrVwEAAAAAknkrQU2Br%2FPoi%2FARdB550Wc0x7E%3DDyg7333SOTN8ZdwJvpP45hIAB74HyJ4dt67blo7CPmu8VaqYTq'
access_token = ['809548229163487233-dt6vwA4BtTI189q85GrRDoJql0MipDb']
access_token_secret = ['Bu67bEV4pO4B7Bwj8klJsUutrnJMBn6w6rJrzLjBMn0uT']

# approved COVID-19 vaccine:
# https://www.canada.ca/en/health-canada/services/drugs-health-products/covid19-industry/drugs-vaccines-treatments/vaccines.html

# need 1000+ posts
# COVID, vaccination, name-brand COVID vaccine

kw_cov = 'covid OR SARS-CoV-2 OR coronavirus '
kw_vac = 'OR vaccination OR Moderna OR Pfizer OR AstraZeneca OR (Janssen AND vaccine) OR (Johnson AND vaccine) OR Covishield OR Covaxin OR Sinopharm OR Sinovac '
kw_tag = 'OR #COVID OR #VACCINATION OR #Moderna OR #Pfizer OR #AstraZeneca OR #Johnson&Johnson OR #Covishield OR #Covaxin OR #Sinopharm OR #Sinovac OR #coronavirus '


def t_auth(i):
    auth = tweepy.OAuthHandler(consumer_key[i], consumer_secret[i])
    auth.set_access_token(access_token[i], access_token_secret[i])
    api = tweepy.API(auth, wait_on_rate_limit=True)

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

    collect(api, "2021-11-28T12:00:00", './output_12.csv')
    #collect(api, "2021-11-30", './output_2.csv')
    #collect(api, "2021-12-1", './output_3.csv')
