from flask import Flask,jsonify,request
import xila
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def ceshi():
    data_up = request.get_json()
    print("data_up:",data_up)
    res = xila.craw()
    print(res)
    return jsonify(res)

if __name__ == '__main__':
    app.run()


