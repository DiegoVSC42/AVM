#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from atproto import Client

import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='pydantic')

def thread(base_url, login, password, messages):
    client = Client(base_url)
    client.login(login, password)

    post = None
    root_post = None

    for message in messages:
        if not post:
            post = client.send_post(message)
            root_post = post
        else:
            post = client.send_post(
                text=message,
                reply_to={
                    'root': {
                        'uri': root_post['uri'],
                        'cid': root_post['cid']
                    },
                    'parent': {
                        'uri': post['uri'],
                        'cid': post['cid']
                    }
                }
            )
