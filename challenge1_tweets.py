#!/usr/bin/env python
# coding: utf-8

# In[20]:


import re
from collections import Counter


# In[25]:


class TweetParser:
    overall_hashtag_counter = Counter([])

    def parse_tweet(self, tweet):
        hashtags = re.findall("#\w*", tweet)
        return hashtags
    
    def main(self, tweet):
        hashtags_list = self.parse_tweet(tweet)
        hashtag_count = Counter(hashtags_list)
        
        # combine both counters
        self.overall_hashtag_counter += hashtag_count
        return

    def print_all_hashtags(self):
        for key, value in self.overall_hashtag_counter.items():
            print(key, ' : ', value)


# In[26]:


tweets = [
    "Worlds best cricketer is #sachin",
    "Best #bunny is white one",
    "Hello #friend, this is me",
    "This is a simple #hastag #example #friend #bunny",
    "What a #wonderful world",
    "best #friend forever",
]


# In[27]:


tweet_parser = TweetParser()

for tweet in tweets:
    tweet_parser.main(tweet)


# In[24]:


tweet_parser.print_all_hashtags()

