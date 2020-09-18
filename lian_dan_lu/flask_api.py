from flask import Flask, jsonify
# import web_spider
import db_1

app = Flask(__name__)


@app.route('/kuaishou/ldl/female')
def api():
    res = db_1.gender_female()
    print(res)
    return jsonify(res)


if __name__ == '__main__':
    app.run("0.0.0.0")
    # app.run("0.0.0.0")
