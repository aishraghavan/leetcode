from design_twitter import Twitter

def trial_game():
    obj = Twitter()
    obj.follow(1,4)
    obj.follow(1,2)
    obj.follow(2,4)
    obj.follow(2,5)
    obj.follow(3,2)
    obj.follow(3,5)
    obj.follow(4,5)

    obj.postTweet(1, 'a')
    obj.postTweet(1, 'b')
    obj.postTweet(3, 'c')
    obj.postTweet(4, 'd')
    obj.postTweet(5, 'e')
    obj.postTweet(2, 'f')
    obj.postTweet(2, 'g')
    obj.postTweet(3, 'h')
    obj.postTweet(5, 'i')
    obj.postTweet(4, 'j')

    for i in range(1,6):
        obj.print_user_data(i)

def test_game():
    obj = Twitter()
    obj.postTweet(1,5)
    print obj.getNewsFeed(1)
    obj.follow(1,2)
    obj.postTweet(2,6)
    #import ipdb; ipdb.set_trace()
    print obj.getNewsFeed(1)
    obj.unfollow(1,2)
    #import ipdb; ipdb.set_trace()
    print obj.getNewsFeed(1)


def test_game_2():
    obj = Twitter()
    obj.postTweet(1,1)
    print obj.getNewsFeed(1)
    obj.follow(2,1)
    print obj.getNewsFeed(2)
    obj.unfollow(2,1)
    print obj.getNewsFeed(2)

if __name__ == "__main__":

    # obj = Twitter()
    # obj.postTweet(1,10)
    # obj.postTweet(1,20)
    # obj.follow(2, 1)
    # obj.follow(3, 1)

    #trial_game()
    #test_game()
    test_game_2()






# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
