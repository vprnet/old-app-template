# If Frozen Flask needs to generate URLs, use this file
# see: http://pythonhosted.org/Frozen-Flask/#url-generators
# if enabled, `python freeze.py build` becomes new build command

#import sys
#from flask_frozen import Freezer
#from skeleton import app
#from upload_s3 import set_metadata
#
#freezer = Freezer(app)
#
#
#@freezer.register_generator
#def name_of_skeleton.py_method():
#    for i in url_list:
#        yield {'variable_name': i}
#
#if __name__ == '__main__':
#    if len(sys.argv) > 1 and sys.argv[1] == 'build':
#        app.debug = False
#        freezer.freeze()
#        set_metadata()
#    else:
#        app.run(debug=True)
