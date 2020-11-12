import os
import flask
import csv
from Gauss import gauss
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.rsplit('.', 1)[1] == 'csv':
            filename = secure_filename(file.filename)
            file.save(os.path.join(filename))
            result = gauss(filename)
            os.remove(os.path.join(filename))
            file.close()
            return flask.render_template(
                'index.html', result=', '.join(str(e) for e in result)
            )
    return flask.render_template(
        'index.html', result = False
    )

if __name__ == '__main__':
   http_server = WSGIServer(('', 5000), app)
   http_server.serve_forever() 

