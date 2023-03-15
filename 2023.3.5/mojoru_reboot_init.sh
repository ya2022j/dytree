


/usr/local/nginx/sbin/nginx  -c /usr/local/nginx/conf/nginx.conf

systemctl restart docker

docker restart $(docker ps -a -q)


#cd /home/d_tree &&

#export PATH=$PATH:/usr/local/python3/bin &&


#gunicorn -w 4 -b 127.0.0.1:8888 --access-logfile access8888.log --error-logfile error8888.log dtree:app -D &&




#echo  'bash /home/mojoru_reboot_init.sh'  >>  /etc/rc.d/rc.local


cd /home/dtree_todolist

nohup ./dtree_todolist  todolist.log 2>1&1 &



cd /home/gtodo/server
nohup ./mini_todo  &

bash
cd /home/gtodo/client


nohup npm run serve  &






