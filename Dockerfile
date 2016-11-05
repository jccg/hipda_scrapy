FROM ubuntu:trusty-20161006

RUN apt-get update

RUN apt-get install -y openssh-server

RUN mkdir /var/run/sshd

RUN echo 'root:password' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

#更换阿里云源
ADD docker/sources.list ./
RUN mv sources.list /etc/apt/sources.list

RUN apt-get clean
RUN apt-get update

#安装nginx和php-fpm和php-mysqli
RUN apt-get install -y nginx
RUN apt-get install -y php5-fpm
RUN apt-get install -y php5-mysql

#配置nginx
RUN mkdir /var/www
RUN mkdir /var/www/html
ADD docker/default ./
RUN mv default /etc/nginx/sites-available/default

#配置php-fpm
ADD docker/www.conf ./
RUN mv www.conf /etc/php5/fpm/pool.d/www.conf

#部署php程序
#ADD docker/index.php /var/www/html/
ADD ./ /var/www/html/

#启动服务脚本
ADD docker/start.sh /root/

EXPOSE 22
EXPOSE 80

#CMD ["sh", "start.sh"]

ENTRYPOINT service nginx start && service php5-fpm start && /usr/sbin/sshd -D 
