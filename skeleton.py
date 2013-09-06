import sys
from upload_s3 import set_metadata

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

# If project doesn't have it's own domain/subdomain, use BASE_URL
#app.config['FREEZER_BASE_URL'] = ''


@app.route('/')
def index():
    return render_template('content.html')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
        set_metadata()
    else:
        app.run(debug=True)
