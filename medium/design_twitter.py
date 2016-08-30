"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and
is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.

getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed.
Each item in the news feed must be posted by users who the user followed or by the user herself.
Tweets must be ordered from most recent to least recent.

follow(followerId, followeeId): Follower follows a followee.

unfollow(followerId, followeeId): Follower unfollows a followee.


https://discuss.leetcode.com/topic/47838/python-solution/2
"""
import heapq
import itertools
from sets import Set
from collections import namedtuple
from copy import deepcopy

Tweet = namedtuple('Tweet', ['id', 'time'])
# class Tweet(object):
#     def __init__(self, id, time):
#         self.id  = id
#         self.time = time
#
#     def __str__(self):
#         return "id {0} : time {1}".format(str(self.id),str(self.time))

#Not needed
# class User(object):
#     pass

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.timer = itertools.count(step =-1)
        self.timer = itertools.count(step =-1)
        self.followees = {}
        self.tweets = {}


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        #if exists
        if self.tweets.get(userId):
            self.tweets[userId].append(Tweet(tweetId, next(self.timer)))
        else:
            self.tweets[userId] = [Tweet(tweetId, next(self.timer))]


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        heap_list = []
        tweet_s = deepcopy(self.tweets.get(userId) if self.tweets.get(userId) else [])
        people_i_follow = self.followees.get(userId)
        if people_i_follow:
            for followee in people_i_follow:
                    tweet_s+= self.tweets.get(followee) if self.tweets.get(followee) else []

        for tweet in tweet_s:
            heapq.heappush(heap_list, (tweet.time,tweet.id))
        # print "tweets", tweets
        # print "heap_list", heap_list

        tweets_list = [t for _, t in itertools.islice(heap_list, 4)]
        #import ipdb; ipdb.set_trace()
        #return heap_list
        return tweets_list


    def follow(self, followerId, leaderId):
        #followeeId -> leaderId
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if leaderId != followerId:
            if self.followees.get(followerId):
                #add more
                self.followees[followerId].add(leaderId)
            else:
                #create new
                self.followees[followerId] = Set([leaderId])


    def unfollow(self, followerId, leaderId):
        #followeeId -> leaderId
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        #only if exists
        if self.followees.get(followerId):
            #remove
            #to prevent key error
            if Set([leaderId]).issubset(self.followees[followerId]):
                self.followees[followerId].remove(leaderId)

    def print_user_data(self, userId):
        print userId
        #print self.followees
        print "Following :", self.followees.get(userId)
        print "Followers :", "we do not care"
        print "Tweets :", self.tweets.get(userId)
        print self.getNewsFeed(userId)
