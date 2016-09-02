"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may
 assume that calls are being made to the system in chronological order
 (ie, the timestamp is monotonically increasing).
 You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);
Follow up:
What if the number of hits per second could be very large? Does your design scale?

Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.

Question: http://www.cnblogs.com/grandyang/p/5605552.html
https://discuss.leetcode.com/topic/48753/java-solution-easy-to-understand/2
https://discuss.leetcode.com/topic/48752/simple-java-solution-with-explanation
https://discuss.leetcode.com/topic/48758/super-easy-design-o-1-hit-o-s-gethits-no-fancy-data-structure-is-needed

"""

class HitCounter(object):
    def __init__(self):
        self.hits = [0]*300
        self.times = [0]*300

    def hit(self, timestamp):
        index = timestamp %300
        if self.times[index]!=timestamp:
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timestamp):
        total = 0
        i = 0
        while i < 300:
            if (timestamp - self.times[i] < 300):
                total += self.hits[i]
            i+=1
        return total
