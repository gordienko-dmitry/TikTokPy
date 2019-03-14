import requests
import time
import urllib.parse
import logging

from .settings import Settings


methods = {
    'get': requests.get,
    'post': requests.post
}


def xor(string, key=5):
    """
    Decode string 
    """
    return ''.join([hex(int(x ^ key))[2:] for x in string.encode('utf-8')])
    
   
def prepare_url(path, query=''):
    """
    Create url with parameters
    """
    host, url = Settings.urls.get(path)
    full_path = url + '?' + query
    url = urllib.parse.urlunparse((Settings.http_prefix, host, url, None, query, ''))
    return url, host, full_path

    
def _https_query(method, path, custom_query={}, custom_headers={}, data=None, ver=1):
    """
    Base method for api

    :param method: method http, POST or GET required
    :param url: url
    :param custom_query:
    :param custom_headers: dict of header params
    :param session: dict of cookies parameters
    :param data:
    :return: result of requests get or post method
    """

    headers = dict(Settings.base_headers)
    headers.update(custom_headers)
    cookies = ''
    for key, value in Settings.cookies.items():
        cookies += '{}={};'.format(key, value)
    headers['Cookie'] = cookies

    time_for_query = str(round(time.time()))
    headers['X-Khronos'] = time_for_query

    query = Settings.query_string
    for key, value in custom_query.items():
        if value is None:
            continue
        query[key] = value
    query['ts'] = time_for_query

    url, host, full_path = prepare_url(path, urllib.parse.urlencode(query))
    headers['Host'] = host

    try:
        response = methods[method.lower()](url, headers=headers, data=data, verify=False)
        print(response.content)
        return response.json()
    except KeyError:
        logging.error('Wrong method: {}'.format(method))
    except Exception as e:
        logging.exception('Unknown error: {}'.format(e))


# ACTIONS


def login(username, password):
    """
    Send username & password, take user info
    :param username:
    :param password:
    :return:
    """

    method = 'get'
    query = dict(Settings.login_data)
    query['username'] = xor(username)
    query['password'] = xor(password)

    return _https_query(method, 'login', custom_query=query)


def get_user_info(user_id):
    """
    Get user info
    """
    method = 'get'
    
    return _https_query(method, 'user_info', custom_query={'user_id': user_id}, ver=2)


def get_followers_list(user_id, count=20, max_time=None):
    """
    Get folowwers
    """
    method = 'get'
    query = {
        'user_id': user_id,
        'count': count,
        'max_time': max_time if max_time else 0, #str(round(time.time())),
        'offset': 0,
        'source_type': 1
    }

    return _https_query(method, 'followers_list', custom_query=query)


def get_following_list(user_id, count=20, max_time=None):
    """
    Get following
    """
    method = 'get'
    query = {
        'user_id': user_id,
        'count': count,
        'max_time': max_time if max_time else 0,
        'offset': 0,
        'source_type': 1
    }

    return _https_query(method, 'followings_list', custom_query=query)


def get_search_results(source, text, count=20):
    """
    Searching by source: discover / challenge / music
    """
    method = 'get'
    query = {
        'cursor': 0,
        'keyword': text,
        'count': count,
        'type': 1,
        'hot_search': 0,
        'type': 1,
        'is_pull_refresh': 0,
        'search_source': source
    }

    return _https_query(method, 'search', custom_query=query)

    
def like_post(post_id, like_type=1):
    """
    Like / unlike post by id
    """
    method = 'post'
    data = 'aweme_id={}&channel_id={}&type={}'.format(post_id, 3, like_type)
    
    return _https_query(method, 'like', custom_query=query, data=data)   


def get_posts(user_id, count=20):
    """
    Get list of posts
    """
    method = 'post'
    query = {
        'min_cursor': 0,
        'max_cursor': 0,
        'user_id': user_id,
        'count': count
    }
    return _https_query(method, 'posts', custom_query=query)

    
def follow(user_id, unfollow=False):
    """
    Follow on user by id
    """
    method = 'get'
    query = {
        'user_id': user_id,
        'channel_id': 3,
        'type': 0 if unfollow else 1
    }

    return _https_query(method, 'follow', custom_query=query)

