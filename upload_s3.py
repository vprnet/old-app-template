#!/usr/local/bin/python
import os
import hashlib
import gzip
import time
from sys import argv
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from config import (AWS_KEY, AWS_SECRET_KEY, AWS_BUCKET, AWS_DIRECTORY,
    HTML_EXPIRES, STATIC_EXPIRES, IGNORE_DIRECTORIES, IGNORE_FILES,
    IGNORE_FILE_TYPES)

content_types = {
    '.css': 'text/css',
    '.js': 'text/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.bmp': 'image/bmp',
    '.gif': 'image/gif',
    '.ico': 'image/ico',
    '.csv': 'text/csv',
    '.html': 'text/html',
    '.svg': 'image/svg+xml',
    '.json': 'text/json'
}


def directory_list(argv, directory='app/build'):
    """Creates a list of all non-excluded files in current directory
    and below"""

    if argv > 1:
        IGNORE_DIRS = IGNORE_DIRECTORIES + argv[1:]

    file_list = []
    for root, dirs, files in os.walk(directory):
        for d in IGNORE_DIRS:
            if d in dirs:
                dirs.remove(d)
        for f in IGNORE_FILES:
            if f in files:
                files.remove(f)
        for f in files:
            ext = os.path.splitext(f)[1]
            if ext in IGNORE_FILE_TYPES:
                files.remove(f)

        file_list.append((root, files))

    return file_list


def s3_filename():
    """Takes list of files to be uploaded and modifies the names so that they
    will be served properly from s3"""

    file_list = directory_list(argv)
    s3_list = []
    for f in file_list:
        for i in f[1]:
            ext = os.path.splitext(i)[1]
            if ext in IGNORE_FILE_TYPES:
                pass
            else:
                if f[0] is not '.':
                    s3_list.append(f[0][10:] + '/' + i)
                else:
                    s3_list.append(i)
    return s3_list


def set_metadata():
    """Take a list of files to be uploaded to s3 and gzip CSS, JS, and HTML,
    setting metadata for all files including an 'expires' header defined
    at the beginning of the file. HTML expires after 1 hour."""

    s3_list = s3_filename()
    conn = S3Connection(AWS_KEY, AWS_SECRET_KEY)
    mybucket = conn.get_bucket(AWS_BUCKET)
    expires = time.time() + STATIC_EXPIRES
    expires_header = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime(expires))

    for filename in s3_list:
        k = Key(mybucket)
        ext = os.path.splitext(filename)[1]
        if ext == '':
            ext = '.html'

        if ext == '.html':  # deletes '.html' from s3 key so no ext on url
            local_name = os.path.splitext(filename)[0]
            if local_name == '/index':
                local_name = '/index.html'
            if local_name[0] != '/':  # if file within child dir
                k.key = AWS_DIRECTORY + '/' + local_name
            else:  # if file in top level dir
                k.key = AWS_DIRECTORY + local_name
            k.set_metadata('Expires', time.time() + HTML_EXPIRES)
        else:
            k.key = AWS_DIRECTORY + '/' + filename  # strip leading 0
            k.set_metadata('Expires', expires_header)

        if ext == '.css' or ext == '.js' or ext == '.html':
            build_file = 'app/build/' + filename
            f_in = open(build_file, 'rb')
            with gzip.open(build_file + '.gz', 'w+') as f:
                f.writelines(f_in)
            f_in.close()
            f = build_file + '.gz'
            k.set_metadata('Content-Encoding', 'gzip')
        else:
            f = 'app/build/' + filename

        print k.key

        k.set_metadata('Content-Type', content_types[ext])
        etag_hash = hashlib.sha1(f + str(time.time())).hexdigest()
        k.set_metadata('ETag', etag_hash)
        k.set_contents_from_filename(f)
        k.make_public()
