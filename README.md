#VPR Project Skeleton
Create and push static files for hosting on Amazon S3.

This stack is used by VPR to publish news apps and can be used for anything from building a blog to creating web applications.

## Technology
- [Flask](http://flask.pocoo.org/): Used for local development

- [Frozen-Flask](http://pythonhosted.org/Frozen-Flask/): Freezes Flask application into a series of static files

- [Jinja](http://jinja.pocoo.org/docs/): Python templating language

- [Bootstrap](http://getbootstrap.com/): Twitter's HTML/CSS/JS framework

- [Sass](http://sass-lang.com/): CSS extension that allows for variables, inheritance, and even logic in stylesheets

## Install 

1. Install [virtualenv](https://pypi.python.org/pypi/virtualenv)
3. Clone the repository

        $ git clone git@github.com:vprnet/project-skeleton.git

4. Enter virtual environment

        $ source venv/bin/activate

5. Install requirements

        $ pip install -r requirements.txt

## Develop

To run local server:

        $ python skeleton.py

The project will be viewable at http://127.0.0.1:5000/

## Deploy

1. Create an S3 bucket to serve content using [Amazon's documentation](http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) for hosting a static website

2. Configure AWS settings in `_settings.py`

3. Rename `_settings.py` to `settings.py`

        $ mv _settings.py settings.py

4. Freeze files

        $ python skeleton.py build

5. Push to S3

        $ python upload_s3.py

## Sass and CSS

If you haven't tried one of the CSS 'meta-languages' (Sass/Less) they are well worth learning (and easy!). If, however, you want to stick to standard CSS you can do so by working with style.css the old fashioned way (though Bootstrap's CSS will be prepended to the stylesheet).

Here are some instructions for developing with Sass:

1. Check out the documentation and examples on the [Sass website](http://sass-lang.com/)

2. Edit `_example.scss`. Valid css is valid scss, so use as much or little Sass as you like.

3. Compile. I use CodeKit (mentioned below). CodeKit compiles Sass into CSS, concatenates all stylesheets, and minifies them for production. Cool.

## To-Do

1. Automate generation of social network meta tags
2. Impliment NPR-API ingest

## Front-End Web Tool
I use [CodeKit](https://incident57.com/codekit/) during front end development. It manages my static assets by concatenating and minifying all of my stylesheets and javascript automatically after any modifications. The "Frameworks" feature lets me utilize base stylesheets across multiple projects while only needing to maintain a single copy of the file.

## Author
[Matt Parrilla](http://twitter.com/mattparrilla)
