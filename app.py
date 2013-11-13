import sys
from upload_s3 import set_metadata
from settings import AWS_BUCKET, AWS_DIRECTORY

from flask import Flask, render_template, request
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

if AWS_DIRECTORY:
    base_url = 'http://' + AWS_BUCKET + '/' + AWS_DIRECTORY
    app.config['FREEZER_BASE_URL'] = base_url
else:
    base_url = 'http://' + AWS_BUCKET

# If Flask is needed to generate URLs, use freezer.register_generator
# see: http://pythonhosted.org/Frozen-Flask/#url-generators


@app.route('/')
def index():
    page_url = base_url + request.path
    social = {
        'title': 'VPR App Template',
        'subtitle': 'Build HTML with Python, serve statically from S3',
        'img': 'http://www.vpr.net/apps/vpr-logo-green-letters.png',
        'description': 'The VPR App Template is available as an open source repository on Github.',
        'twitter_text': 'This VPR App Template is awesome!! You should check it out',
        'twitter_hashtag': 'dotCom'
    }

    return render_template('content.html', social=social, page_url=page_url)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
        set_metadata()
    else:
        app.run(debug=True)
