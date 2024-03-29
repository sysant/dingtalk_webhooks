1.封装钉钉机器人, 为cloudflare webhooks
2.python3.x  pip3 install -r requit.txt
3. 将gunicorn.service 放到/usr/lib/systemd/system下 执行systemctl daemon-reload
4. 将gunicorn.conf.py 复制到 /etc/下
5. systemctl start gunicorn.service 启动服务

