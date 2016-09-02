from design_hit import HitCounter

if __name__ == "__main__":
    counter = HitCounter()
    #hit at timestamp 1.
    counter.hit(1)

    #hit at timestamp 2.
    counter.hit(2)

    #hit at timestamp 3.
    counter.hit(3)

    #get hits at timestamp 4, should return 3.
    print counter.getHits(4)

    #hit at timestamp 300.
    counter.hit(300)

    #get hits at timestamp 300, should return 4.
    print counter.getHits(300)

    #get hits at timestamp 301, should return 3.
    print counter.getHits(301)

    #import ipdb; ipdb.set_trace()
    counter.hit(320)
    counter.hit(320)

    print counter.getHits(301)
    print counter.getHits(10)
