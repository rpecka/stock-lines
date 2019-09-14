#C:\Users\Daniel\Desktop\realDonaldTrump_tweets

import csv
from datetime import datetime

def categorize_tweets (day_categories):
    date_tweets = read_date_file()
    categorized = []
    for date,category in day_categories.items():
        tweet_text = date_tweets.get(date)
        if tweet_text is not None:
            categorized.append((tweet_text,category))
    return categorized

def read_date_file():
    date_tweets = {}
    with open(r"C:\Users\Daniel\Desktop\date_tweets.csv") as date_tweet_file:
        reader = csv.reader(date_tweet_file)
        for row in reader:
            date_tweets[row[0]]= row[1]
    return date_tweets

def make_date_file():
    with open(r"C:\Users\Daniel\Desktop\realDonaldTrump_tweets.csv") as raw_tweets:
        reader = csv.reader(raw_tweets)
        next(reader)
        date_tweets = {}
        for row in reader:
            raw_date = row[1]
            datetime_object = datetime.strptime(raw_date, '%Y-%m-%d %H:%M:%S')
            date = datetime_object.date()
            existing = date_tweets.get(date)
            if existing is not None:
                date_tweets[date] = existing + ';' + row[2]
            else:
                date_tweets[date] = row[2]
    with open(r"C:\Users\Daniel\Desktop\date_tweets.csv",'w') as date_tweeet_file:
        writer = csv.writer(date_tweeet_file)
        writer.writerows(date_tweets.items())


#2019-09-07  8:44:53 PM
if __name__ == '__main__':
#    make_date_file()
    day_categories = {str(datetime.strptime("2019-09-14 14:57:43", '%Y-%m-%d %H:%M:%S').date()):'sad'}
    print (categorize_tweets(day_categories))