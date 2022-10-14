import snscrape.modules.twitter as snst
import pandas as pd
import math

query = "(#climatechange) lang:en until:2022-04-23 since:2022-01-01"
tweets = []
count = 0

for tweet in snst.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break

    if tweet.inReplyToTweetId is not None: # don't want reply
        continue
    if tweet.quotedTweet is not None:
        tweets.append([tweet.user.id, tweet.user.username, tweet.user.description, tweet.id, tweet.content, tweet.quotedTweet.id,tweet.mentionedUsers,tweet.quoteCount,tweet.retweetCount,tweet.replyCount,tweet.likeCount])
    else:
        tweets.append([tweet.user.id, tweet.user.username, tweet.user.description,tweet.id,tweet.content,0,tweet.mentionedUsers,tweet.quoteCount,tweet.retweetCount,tweet.replyCount,tweet.likeCount])
    count+=1
    print(count)
df = pd.DataFrame(tweets, columns=['user_id','user_name','user_description','tweet_id','content','quotedTweet_id','mentionedUsers','#quote','#retweet','#reply','#like'])

#to save to csv
df.to_csv('before_clear_tweets.csv')


