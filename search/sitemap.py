import json
import string

# import ahocorasick
# from urllib.parse import urlparse
from urlparse import urlparse

import random

class Sitemap_generator:

    @staticmethod
    def _tree_build(ver, level):
        if not level:
            ver['size'] = random.randint(1, 10000)
            return ver

        ver['children'] = []
        for key in level.keys():
            child = {'name': key}
            child = Sitemap_generator._tree_build(child, level[key])
            ver['children'].append(child)

        return ver

    @staticmethod
    def _tokenize_url_path(url):
        url_path = urlparse(url).path.strip('/')
        url_path_tokens = url_path.split('/')
        if not url_path_tokens[0]:
            return []
        return url_path_tokens

    @staticmethod
    def build_site_map(start_url, urls):
        site_map = {}
        urls_tokens = []
        for url in urls:
            url_tokens = Sitemap_generator._tokenize_url_path(url)
            urls_tokens.append(url_tokens)

        for ind, url_tokens in reversed(list(enumerate(urls_tokens))):
            level = site_map
            for token in url_tokens:
                cur_val = level.get(token)
                if not cur_val:
                    level[token] = {}
                level = level[token]

        root = {"name": start_url}
        root_tokens = Sitemap_generator._tokenize_url_path(start_url)
        try:
            level = site_map
            for token in root_tokens:
                level = level[token]
        except TypeError:
            level = {}

        tree = Sitemap_generator._tree_build(root, level)
        return tree