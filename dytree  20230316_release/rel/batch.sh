






cd /home/d_tree;
export PATH=$PATH:/usr/local/python3/bin;

gunicorn -w 4 -b 127.0.0.1:8888 --access-logfile access8888.log --error-logfile error8888.log dtree:app -D;





/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf;


