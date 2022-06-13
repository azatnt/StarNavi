#!/usr/bin/python


"""
Generates random users, authenticate, create post by random user and like posts.
"""

import string
import os
import sys
import random
import environ




if __name__ == "__main__":
    project_path = '' # here set your project path, example = /Users/aza/PycharmProjects/StarNavi/
    sys.path.append(project_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()
from config.settings import BASE_DIR
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
import requests
import json
from app.models import Post


def get_random_string(length, stringset=string.ascii_letters):
    return ''.join([stringset[i % len(stringset)] for i in [x for x in os.urandom(length)]])


def create_users(n):
    print("Generating %s user(s)..." % n)
    print("%s\t%s" % ("#", "username"))
    datas = []
    for user_index in range(n):
        url = env('SERVER_HOST') + '/auth/register/'
        password = get_random_string(10)
        data = {
            'username': get_random_string(8),
            'password1': password,
            'password2': password
        }
        response = requests.post(url, data)
        username = json.loads(response.content)['user']['username']
        del data['password2']
        data['password'] = data.pop('password1')
        datas.append(data)

        t = "#%s\t%s"
        print(t % (
            user_index+1,
            username
        ))
        print("")
    with open('users_auth.json', 'w') as jsonfile:
        json.dump(datas, jsonfile)


def authenticate():
    login_url = env('SERVER_HOST') + '/auth/login/'
    file = open('users_auth.json')
    data = json.load(file)
    for i in data:
        auth = {"username": i["username"],
                "password": i["password"]}
        response = requests.post(url=login_url, data=auth)
        token = json.loads(response.content)['access_token']
        yield token


def create_post():
    file = open('users_auth.json')
    data = json.load(file)
    login_url = env('SERVER_HOST') + '/auth/login/'
    for token in authenticate():
        headers = {
            "Authorization": "Bearer " + token
        }
        max_posts_per_user = env('MAX_POSTS_PER_USER', default = 3)
        n = random.randint(1, max_posts_per_user)
        for i in range(n):
            create_post_url = env('SERVER_HOST') + '/api/post/create/'
            body = {
                "title": get_random_string(15),
                "description": get_random_string(40)
            }
            response = requests.post(url=create_post_url, data=body, headers=headers)
            print(json.loads(response.content)['message'])


def like_post():
    post_ids = list(Post.objects.values_list('id', flat=True))
    for token in authenticate():
        headers = {
            "Authorization": "Bearer " + token
        }
        max_likes_per_user = env('MAX_LIKES_PER_USER', default = 3)
        n = random.randint(1, max_likes_per_user)
        for i in range(n):
            random_id = random_num = random.choice(post_ids)
            like_post_url = env('SERVER_HOST') + '/api/post/{}/like/'.format(random_id)
            response = requests.post(url=like_post_url, headers=headers)
            print(json.loads(response.content)['message'])

        headers = {}

def main(argv):
    create_users(env('NUMBER_OF_USERS', default = 3))
    create_post()
    like_post()


if __name__ == "__main__":
    main(sys.argv[0:])