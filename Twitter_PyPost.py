import tweepy
import random
import time

count = 1
for rep in range(5000):
    print 'Run count is ', count
#---------------------------------ACCOUNT #1------------------------------#

#OAuth for Account #1 - 'LongestTwsitera / intern@l'
    consumer_key1=""
    consumer_secret1=""

    access_token1=""
    access_token_secret1=""

    auth1 = tweepy.OAuthHandler(consumer_key1, consumer_secret1)
    auth1.set_access_token(access_token1, access_token_secret1)

    api1 = tweepy.API(auth1)

#Tweet out the message to your account
    for i in range(1):
        randomInt = random.randint(1, 555555554)
        randomInt = str(randomInt)
        strItems = ['#Analytics trending today ','#UI future optimized ','@webtrends think smart for customers ',
                    'Today is the first day ','Future is now ','iPad #app webtrends ','Download #webtrends #app ',
                    '#app for analytics @webtrends ']
        randomTweet = random.choice(strItems)
        time.sleep(10)
        api1.update_status(randomTweet + randomInt + str(count))
        print 'LongestTwistera has posted ' + str(count) + ' tweet(s)'

#Account #1 - Storing Account #2 timeline
    twitter_Name1 = 'LongestTwistera'
    public_tweets1 = tweepy.api.user_timeline(twitter_Name1)
    status_object1 = public_tweets1[0]
    user_object1 = status_object1.user

#---------------------------------ACCOUNT #2------------------------------#

#OAuth for Account #2 - 'TestyTesterror / intern@l'
    consumer_key2=""
    consumer_secret2=""

    access_token2=""
    access_token_secret2=""

    auth2 = tweepy.OAuthHandler(consumer_key2, consumer_secret2)
    auth2.set_access_token(access_token2, access_token_secret2)

    api2 = tweepy.API(auth2)

#Tweet out the message to your account
    for i in range(1):
        randomInt = random.randint(555555555, 999888777)
        randomInt = str(randomInt)
        strItems = ['#Analytics trending today ','#UI future optimized ','@webtrends think smart for customers ',
                    'Today is the first day ','Future is now ','iPad #app webtrends ','Download #webtrends #app ',
                    '#app for analytics @webtrends ']
        randomTweet = random.choice(strItems)
        time.sleep(10)
        api2.update_status(randomTweet + randomInt + str(count))
        print 'TestyTesterror has posted ' + str(count) + ' tweet(s)'
    
#Account #2 - Storing Account #2 timeline
    twitter_Name2 = 'TestyTesterror'
    public_tweets2 = tweepy.api.user_timeline(twitter_Name2)
    status_object2 = public_tweets2[0]
    user_object2 = status_object2.user




#-----------------------RETWEET BETWEEN BOTH ACCOUNTS--------------------------#

#Account #1 - Retweet from Account #2 last tweet
    time.sleep(150)
    reTweetID1 = status_object2.id_str
    print reTweetID1 
    print 'LongestTwistera has retweeted TweetID ' + reTweetID1
    api1.retweet(reTweetID1)

#Account #2 - Retweet from Account #1 last tweet
    time.sleep(150)
    reTweetID2 = status_object1.id_str
    print 'TestyTesterror has retweeted TweetID ' + reTweetID2
    api2.retweet(reTweetID2)
    

#-----------------------REPLY BETWEEN BOTH ACCOUNTS--------------------------#

#Account #1 - Retweet from Account #2 last tweet
    time.sleep(100)
    reTweetID1 = status_object2.id
    api1.update_status("@"+ twitter_Name2 + ' a reply ' + str(randomInt)+str(count), in_reply_to_status_id = reTweetID1)
    print twitter_Name1 + ' has replied to a tweet posted by ' + twitter_Name2 + ' ' + str(count) + ' times'

#Account #2 - Retweet from Account #1 last tweet
    time.sleep(100)
    reTweetID2 = status_object1.id
    api2.update_status("@"+ twitter_Name1 + ' a reply ' + str(randomInt)+str(count), in_reply_to_status_id = reTweetID2)
    print twitter_Name2 + ' has replied to a tweet posted by ' + twitter_Name1 + ' ' + str(count) + ' times'

    count = count + 1
