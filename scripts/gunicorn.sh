#!/usr/bin/bash
cp /home/ubuntu/devops-app/gunicorn/gunicorn.socket  /etc/systemd/system/gunicorn.socket
cp /home/ubuntu/devops-app/gunicorn/gunicorn.service  /etc/systemd/system/gunicorn.service

systemctl start gunicorn.service
systemctl enable gunicorn.service
