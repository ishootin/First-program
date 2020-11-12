
import flask
import csv
from primarity import is_prime, euler_func
from Gauss import gauss
from flask import Flask, request
from gevent.pywsgi import WSGIServer

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )

@app.route('/gauss')
def Gauss():
    exampleFile = open('fileupload.csv', encoding = 'UTF-8')
    exampleReader = csv.reader(exampleFile, delimiter = ';')
    n = 0
    for row in exampleReader:
        n += 0
    a = numpy.zeros((n,n+1))

    for row in exampleReader:
        for value in row:
            a[row][value] = value 
        print(string)
    exampleFile.close()

    return flask.render_template(
        'gauss.html',
        name = name_param,
        ans = gauss(name_param),
        method=request.method
    )
    

if __name__ == '__main__':
   http_server = WSGIServer(('', 5000), app)
   http_server.serve_forever() 
   app.run(debug = True, host="0.0.0.0", port="5000")
