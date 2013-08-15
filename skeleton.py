import sys

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

DEBUG = True


@app.route('/')
def index():
    return render_template('content.html')


@app.route("/xml")
def xml():
    return render_template('nprml.xml',
                            link=link,
                            title=title,
                            subtitle=subtitle,
                            teaser=teaser,  # label teaser par with id="teaser" and scrape from page
                            storyDate=storyDate,
                            pubDate=pubDate,
                            tags=tags,
                            bylines=bylines,
                            image=image)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
        # call upload.py here?
        # if sys.argv[2] == 'y':
            #upload()
    else:
        app.run()
