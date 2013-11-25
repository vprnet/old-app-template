from app import app
from flask import render_template, request
from config import BASE_URL


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    social = {
        'title': 'VPR App Template',
        'subtitle': 'Build HTML with Python, serve statically from S3',
        'img': 'http://www.vpr.net/apps/vpr-logo-green-letters.png',
        'description': 'The VPR App Template is available as an open source repository on Github.',
        'twitter_text': 'This VPR App Template is awesome!! You should check it out',
        'twitter_hashtag': 'dotCom'
    }

    return render_template('content.html', social=social, page_url=page_url)
