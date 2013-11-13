# Amazon S3 Settings
AWS_KEY = 'REQUIRED'
AWS_SECRET_KEY = 'REQUIRED'
AWS_BUCKET = 'REQUIRED'
AWS_DIRECTORY = ''  # Leave blank *not false* unless project not at base URL
                    # i.e. example.com/apps/ instead of example.com/

# Cache Settings (units in seconds)
STATIC_EXPIRES = 60 * 24 * 3600
HTML_EXPIRES = 3600

# Upload Settings (ignores anything included below)
IGNORE_DIRECTORIES = ['.git', 'venv', 'sass', 'templates']
IGNORE_FILES = ['.DS_Store']
IGNORE_FILE_TYPES = ['.gz', '.pyc', '.py', '.rb', '.md']
