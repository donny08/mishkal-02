#!/usr/bin/python3
# -*- coding=utf-8 -*-
import sys
from bottle import Bottle, run
from bottle import static_file
from bottle import template
from bottle import view
from bottle import get
from bottle import request
from bottle import response
from bottle import TEMPLATE_PATH

import datetime
import logging
import json
import os.path
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../../'))
import core.adaat
app = Bottle()
#~ xpath = os.path.join(os.path.dirname(__file__), 'views')
xpath = os.path.dirname(os.path.realpath(__file__))
#~ print("xpath", xpath)
TEMPLATE_PATH.insert(0, os.path.join(xpath, "views"))

#----------------------------------
# define logger
# prepare logging 
#---------------------------------
d = os.path.dirname(sys.argv[0])
LOG_FILENAME = os.path.join(d,u'tmp','logging_mishkal.out')
logging.basicConfig(filename = LOG_FILENAME,level=logging.INFO,)
myLogger = logging.getLogger('Mishkal')
h = logging.StreamHandler() # in production use WatchedFileHandler or RotatingFileHandler
h.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
myLogger.addHandler(h)
myLogger.setLevel(logging.INFO) # in production use logging.INFO


def writelog(text,action):
    """
    @param text: an object to be logged
    @type text: object
    """
    pass;
    timelog = datetime.datetime.now().strftime("%Y-%m-%d %I:%M");
    textlog = u"\t".join([timelog, action, text]);
    #~ myLogger.info(textlog);
#------------------
# resources files
#------------------
@app.route('/_files/fonts/<filename>')
def send_image(filename):
    path = os.path.join(xpath,'./resources/files/fonts' ) 
    return static_file(filename, root= path)

@app.route('/_files/xzero-rtl/css/<filename>')
def send_image(filename):
    path = os.path.join(xpath,'./resources/files/xzero-rtl/css' ) 
    return static_file(filename, root= path)

@app.route('/_files/xzero-rtl/js/<filename>')
def send_image(filename):
    path = os.path.join(xpath, './resources/files/xzero-rtl/js') 
    return static_file(filename, root= path)

@app.route('/_files/xzero-rtl/fonts/<filename>')
def send_image(filename):
    path = os.path.join(xpath,'./resources/files/xzero-rtl/fonts' ) 
    return static_file(filename, root= path)

@app.route('/_files/samples/<filename:re:.*\.(png|jpg|jpeg)>')
def send_image(filename):
    path = os.path.join(xpath, './resources/files/samples' ) 
    writelog("path", path)
    return static_file(filename, root= path,  mimetype='image/png')


@app.route('/_files/images/<filename:re:.*\.(png|jpg|jpeg)>')
def send_image(filename):
    path = os.path.join(xpath,'./resources/files/images') 
    return static_file(filename, root= path, mimetype='image/png')

@app.route('/_files/<filename>')
def send_image(filename):
    path = os.path.join(xpath,'./resources/files' ) 
    return static_file(filename, root= path)


#---------------
# Adawats
#---------------
@app.route('/')
@app.route('/main')
@app.route('/index')
#~ @view(os.path.join(xpath, 'views/main2'))
@view('main2')
def main():
    return {'DefaultText':core.adaat.random_text(),
      'ResultText':u"السلام عليكم",
      }

@app.route('/ajaxGet')
@app.route('/mishkal/ajaxGet')
def ajaxget():
    """
    this is an example of using ajax/json
    to test it visit http://localhost:8080/ajaxGet"
    """    
    text = request.query.text or u"تجربة"
    action = request.query.action or 'DoNothing'
    order = request.query.order or '0'
    options = {};
    options['lastmark'] = request.query.lastmark or '1'
    if sys.version_info[0] < 3:
       text = text.decode('utf-8')
       options['lastmark']  = options['lastmark'].decode('utf8')

    writelog(text,action);
    #Handle contribute cases
    if action=="Contribute":
        return {'result':u"شكرا جزيلا على مساهمتك."}
    resulttext = core.adaat.DoAction(text ,action, options)
    
    #-----------
    # prepare json
    #-------------
    response.set_header("Access-Control-Allow-Methods",     "GET, POST, OPTIONS")
    response.set_header("Access-Control-Allow-Credentials", "true")
    response.set_header( "Access-Control-Allow-Origin",      "*")
    response.set_header("Access-Control-Allow-Headers",     "Content-Type, *")
    response.set_header( "Content-Type", "application/json")
    
    return json.dumps({'result':resulttext, 'order':order})



#------------------
# Static pages files
#------------------

@app.route('/mishkal/<filename>')
def server_static(filename):
    if filename in ("doc", "projects", "contact", "download","index"):
        path = os.path.join(xpath,'./resources/static/') 
        return static_file(filename+".html", root=path)
    else:
        return "<h2>Page Not found</h2>"

#------------------
# actions files
#------------------

@app.route('/<action>/<data>')            # matches /follow/defnull
def user_api(action, data):
    return "action %s, data %s"%(action, data)
from bottle import error

#------------------
# Error Pages
#------------------

@app.error(404)
def error404(error):
    return 'Nothing here, sorry'
if __name__ == '__main__':
    try:
        run(app, server="paste", host='127.0.0.1', port=8080, debug=True)
    except:
        run(app, server="paste", host='127.0.0.1', port=8082, debug=True)    


