import feedparser
import time

# Google's News RSS feed 
NewsFeed = feedparser.parse("https://news.google.com/news/rss")
entry = NewsFeed.entries[1]

# title of news feed, link to article and date/time of feed
print "************"
print entry.title
print "------------News Link----------------"
print entry.link
print "************"
print entry.published
