#from datetime import date
from flask import Flask, request, jsonify
import socket
#import os

app = Flask(__name__)

@app.route('/')
def main():
    return jsonify(
        hostname=socket.gethostname(),
        requestIP=request.remote_addr
    )
if __name__ == '__main__':
    app.run(debug=True, port=8080)