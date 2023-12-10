
#!/usr/bin/bash

 systemctl daemon-reload
 rm -f /etc/nginx/sites-enabled/default

 cp /home/ubuntu/devops-app/nginx/nginx.conf /etc/nginx/sites-available/blog
 ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled/
# ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled
# nginx -t
 gpasswd -a www-data ubuntu
 systemctl restart nginx

