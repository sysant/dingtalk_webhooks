import json
import requests
import sys

from flask import Flask, request, abort, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return abort(401)

@app.route('/robots.txt')
def robots_txt():
    return render_template("robots.txt")

@app.route('/alert', methods = ['GET', 'POST'])
def alert():
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    url = 'https://oapi.dingtalk.com/robot/send?access_token=**************************cfac89a'
    msg={}
    if request.values.get('token') == "wCV7*******************2aI9":
        for key in request.values.keys():
            if key != "token":
                if request.values.get(key) == "":
                    msg.update(json.loads(key))
                else:
                    msg[key] = request.values.get(key)
        if not msg:
            msg.update(request.json)
        #data = {"msgtype": "text", "text": {"content": "aliyun \r\n %s" % str(msg).decode("unicode-escape") }}
        data = {"msgtype": "text", "text": {"content": "aliyun \r\n %s" % str(msg)}}
        r = requests.post(url, data = json.dumps(data), headers = headers)
        res = json.loads(r.text)
        if res.get("errcode", -1) == 0 and res.get("errmsg", "fail") == "ok":
            return jsonify(str(res)), 200
        else:
            return jsonify(str(res)), 400
    else:
        return abort(401)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
