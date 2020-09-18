from flask import Flask, abort, jsonify, make_response, request
import test_1

app = Flask(__name__)


@app.route('/')
def spi():
    res = test_1.reg()
    return res


if __name__ == '__main__':
    app.run(debug=True, host='', port=9000)
