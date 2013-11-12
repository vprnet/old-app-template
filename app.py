import sys
from upload_s3 import set_metadata

from flask import Flask, render_template, request
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

# If project doesn't have it's own domain/subdomain, use BASE_URL
# app.config['FREEZER_BASE_URL'] = 'http://www.example.com/not_base'

# If Flask is needed to generate URLs, use freezer.register_generator
# see: http://pythonhosted.org/Frozen-Flask/#url-generators


@app.route('/')
def index():

    social = {'facebook_url': 'https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fparse.com',
        'twitter_url': 'http://www.twitter.com',
        'google_url': 'http://www.google.com'}
    print request.path
    return render_template('content.html', social=social)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
        set_metadata()
    else:
        app.run(debug=True)
