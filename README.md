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
2. Clone the repository

        $ git clone git@github.com:vprnet/project-skeleton.git

3. Create Virtual Environment in project

        $ cd project-skeleton
        $ virtualenv venv
        
4. Enter virtual environment

        $ source venv/bin/activate

5. Install requirements

        $ pip install -r requirements.txt

6. Change `_settings.py` to `settings.py`

        $ mv _settings.py settings.py
These settings can be configured later (see "Deploy" below)


##Develop

To run local server:

        $ python skeleton.py

The project will be viewable at http://127.0.0.1:5000/

## Deploy

1. Create an S3 bucket to serve content using [Amazon's documentation](http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) for hosting a static website

2. Configure AWS settings in `settings.py`

4. Freeze files and push to S3

        $ python skeleton.py build

## Sass and CSS

If you haven't tried one of the CSS 'meta-languages' (Sass/Less) they are well worth learning (and easy!). If, however, you want to stick to standard CSS you can do so by working with style.css the old fashioned way (though Bootstrap's CSS will be prepended to the stylesheet).

Here are some instructions for developing with Sass:

1. Check out the documentation and examples on the [Sass website](http://sass-lang.com/)

2. Edit `_example.scss`. Valid css is valid scss, so use as much or little Sass as you like.

3. Compile. I use CodeKit (mentioned below). CodeKit compiles Sass into CSS, concatenates all stylesheets, and minifies them for production. Cool.

## To-Do

1. Automate generation of social network meta tags
2. Impliment NPR-API ingest

## Author
[Matt Parrilla](http://twitter.com/mattparrilla)

##Copyright and License

Copyright 2013 Vermont Public Radio

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License.
You may obtain a copy of the License in the LICENSE file, or at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language
governing permissions under the License.
