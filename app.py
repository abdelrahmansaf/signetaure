from os import name
from flask import Flask
from verify import verify
from signe import signe
import base64

app = Flask(__name__)


@app.route('/')
def home():
    return 'essayer /sign ou /verify'


@app.route('/sign')
def signeF():
    return signe()


@app.route('/verify')
def veri():
    return verify()


@app.route('/pubcert')
def pubc():
    return open("public.key").read()


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)
