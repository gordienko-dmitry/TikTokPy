import logging

from . import api


def need_to_login(func):
    """
    Decorator for login function
    """
    def wrapper(self, *args, **kwargs):
        if not self.cookies.get('user_id') or need_to_login:
            response = api.login(self.username, self.password)
            if response:
                self.cookies.update(response['data'])
        if self.cookies.get('user_id'):
            return func(self, *args, **kwargs)
        logging.debug('Wrong username or password')
        raise Exception('Wrong username or password')
    return wrapper


class TikTok():

    def __init__(self, username, password):
        self.cookies = {}
        self.username = username
        self.password = password

    def login(self):
        response = api.login(self.username, self.password)
        if response:
            self.cookies.update(response)
        
    def get_followers_list(self, user_id=None, count=20):
        user_id = user_id if user_id else self.cookies.get('user_id')
        return api.get_followers_list(user_id, count)

    def search_hashtag(self, text, count=20):
        return api.get_search_results('challenge', text, count)
        
    @need_to_login
    def like_followers_posts(self, count=20):
        followers = self.get_followers_list(count)['followers']
        if not followers:
            return
        for follower in followers['followers']:
            posts = api.get_posts(follower.uid)
            if not posts:
                continue
            for post in posts['aweme_list']:
                api.like_post(post['aweme_id'])

    @need_to_login
    def following_followers(self, count):
        followers = self.get_followers_list(count)
        for follower in followers['followers']:
            api.follow(follower.uid)
            
    @need_to_login
    def like_search_results(self, text, count=20):
        search_results = self.search_hashtag(text, count)
        if not search_results:
            return
        for post in search_results['aweme_list']:
            api.like_post(post['aweme_id'])

