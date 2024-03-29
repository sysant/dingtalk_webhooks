1.封装钉钉机器人, 为cloudflare webhooks
2.python3.x  pip3 install -r requit.txt
3. 将gunicorn.service 放到/usr/lib/systemd/system下 执行systemctl daemon-reload
4. 将gunicorn.conf.py 复制到 /etc/下
5. systemctl start gunicorn.service 启动服务
6. yum install nginx -y ;将dingtalk.conf 复制/etc/nginx/conf.d/下；nginx -t检查nginx配置
7. 本地测试 python3 test.py
"{'errcode': 0, 'errmsg': 'ok'}"
钉钉群组中提示，刚表示成功
aliyun 
 {'name': 'hahah', 'pass': 'pass'}

