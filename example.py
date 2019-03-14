import tiktokpy
import os

username = os.environ['username']
password = os.environ['password']

tiktok = tiktokpy.TikTok(username, password)

# go and follow on 30 my followers
tiktok.following_followers(30)

# search posts with hashtag 'cats' and like it
tiktok.like_search_results('cats')

# like 20 (default) posts of my followers
tiktok.like_followers_posts()
