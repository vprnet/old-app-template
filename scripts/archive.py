#!/usr/local/bin/python

from jinja2 import Environment, PackageLoader
from feed import rss_feed


def archive_html():
    env = Environment(loader=PackageLoader('archive', '../templates'))
    template = env.get_template('archive.html')
    rss_list = rss_feed('Coping') #  Normally TS Irene

    resp = template.render(rss_list=rss_list)
    with open('../templates/api.html', 'w+') as f:
        f.write(resp)

archive_html()
