#!/usr/local/bin/python
import requests
import urllib
import json
import Image
import ImageOps
import xml.etree.ElementTree as ET
from datetime import datetime
from cStringIO import StringIO
from bs4 import BeautifulSoup


size = 220, 165


def api_feed(tag):
    tag = {'TS Irene': '176672485', 'Mapping': '191406265'}

    url = ('http://api.npr.org/query?' +
        'orgid=692&fields=title,storyDate,image' +
        '&sort=dateDesc&output=JSON&numResults=5&apiKey=' +
        'MDAyMTYyNjQyMDEyMjg5MzU3MTRhNDY5MA001&id=')

    query = url + tag_id

    r = requests.get(query)
    j = json.loads(r.text)
    stories = j['list']['story']

    story_list = []
    for story in stories:
        try:
            image_url = story['image'][0]['crop'][0]['src']
            print image_url
            image = generate_thumbnail(image_url)
        except KeyError:
            image = 'static/img/thumbnails/irene-thumb.jpg'
        link = story['link']
        date = convert_date(story['storyDate']['$text'])
        title = story['title']['$text']
        story_list.append({
            'title': title,
            'date': date,
            'link': link,
            'image': image,
        })
    return story_list

def generate_thumbnail(image_url):
    thumbnail_path = 'static/img/thumbnails/'
    unicorn = image_url
    filename = unicorn.rsplit('/', 1)[1]
    f = thumbnail_path + filename
    f_save = '../' + f

    img_file = urllib.urlopen(image_url)
    img = StringIO(img_file.read())
    image = Image.open(img)
    im = ImageOps.fit(image, size, Image.ANTIALIAS)
    im.save(f_save)
    return f


def rss_feed(tag):
    rss_list = []
    rss_term = {'TS Irene':
                'http://www.vpr.net/archive_tag_rss/tropical_storm_irene/',
                'Anniversary':
                'http://www.vpr.net/archive_tag_rss/irene_anniversary/',
                'Coping':
                'http://www.vpr.net/archive_tag_rss/graham_frock/'
    }
    r = requests.get(rss_term[tag])
    root = ET.fromstring(r.text)
    for story in root.iter('item'):
        title = story[0].text
        link = story[1].text
        date = convert_date(story[4].text)
        image = get_img(link)
        rss_list.append({
            'title': title,
            'date': date,
            'link': link,
            'image': image
        })

    return rss_list

def get_img(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    image_url = None
    for img in soup.find_all('img'):
        if img.parent.div:
            image = img['src']
            image_url = generate_thumbnail(image)
    if image_url is None:
        image_url = 'static/img/thumbnails/irene-thumb.jpg'
    return image_url

def convert_date(timestamp):
    day = timestamp[5:7]
    month = datetime.strptime(timestamp[8:11], '%b').strftime('%B')
    year = timestamp[12:16]
    date = month + ' ' + day + ", " + year
    return date
