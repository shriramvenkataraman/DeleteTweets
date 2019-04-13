import argparse
import json
import twitter
import io
import csv
import time

# Importing the config file

with open('config.json') as config_file:
    config = json.load(config_file)

class Destroyer(object):
    def __init__(self, twitter_api):
        self.twitter_api = twitter_api

    def delete(self, tweet_id):
        try:
            print("delete tweet %s" % tweet_id)
            self.twitter_api.DestroyStatus(tweet_id)
            time.sleep(0.5)
        except twitter.error.TwitterError as err:
            code = err.args[0][0]['code']
            if code == 144:
                pass

def delete(csv_file):

        api = twitter.Api(consumer_key=config["consumer_key"],
                          consumer_secret=config["consumer_secret"],
                          access_token_key=config["access_key"],
                          access_token_secret=config["access_secret"])
        
        destroyer = Destroyer(api)

        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                destroyer.delete(row["tweet_id"])

        print("Number of deleted tweets: %s\n" % count)

def main():

    consumer_key = config["consumer_key"]
    consumer_secret = config["consumer_secret"]
    access_key = config["access_key"]
    access_secret = config["access_secret"]

    delete("tweets.csv")


if __name__ == "__main__":
    main()
