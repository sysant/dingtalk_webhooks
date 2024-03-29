import requests

post_data={
"name":"hahah",
"pass":"pass"
}

res=requests.post(url="http://127.0.0.1/alert?token=wCV7*************aI9",data=post_data)   ## token参考main.py
