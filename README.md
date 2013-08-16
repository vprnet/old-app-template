#VPR Project Skeleton
The included files make up the VPR project skeleton for news apps.

This project contains code that is unique to VPR, primarily SASS/CSS. Eventually I plan to replace these files with a bootstrap example template.

## Technology
- [Flask](http://flask.pocoo.org/)
Used for local development

- [Frozen-Flask](http://pythonhosted.org/Frozen-Flask/)
Freezes Flask application into a series of static files

- [Jinja](http://jinja.pocoo.org/docs/)
Python templating language

- [Bootstrap](http://getbootstrap.com/)
Twitter's HTML/CSS/JS framework

- [boto](http://docs.pythonboto.org/en/latest/)
Python interface to Amazon Web Services (for deploying project to S3)

- [Sass](http://sass-lang.com/)
CSS extension that allows for variables, inheritance, and even logic in stylesheets

## Install 

1. Install [virtualenv](https://pypi.python.org/pypi/virtualenv)
3. Clone the repository

        $ git clone git@github.com:vprnet/project-skeleton.git

4. Enter virtual environment

        $ source venv/bin/activate

5. Install requirements

        $ pip install -r requirements.txt

## To-Do

1. Automate generation of social network meta tags
2. Impliment NPR-API ingest
3. Completely remove VPR specific code from project skeleton

## Front-End Web Tool
I use [Codekit](https://incident57.com/codekit/) during front end development. It manages my static assets by concatenating and minifying all of my stylesheets and javascript automatically after any modifications. The "Frameworks" feature lets me utilize base stylesheets across multiple projects while only needing to modify or maintain a single copy of the file.

## Author
[Matt Parrilla](http://twitter.com/mattparrilla)
