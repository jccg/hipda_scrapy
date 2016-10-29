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

#安装nginx和php-fpm
RUN apt-get install -y nginx
RUN apt-get install -y php5-fpm

#配置nginx
RUN mkdir /var/www
RUN mkdir /var/www/html
RUN sed -ri 's:/usr/share/nginx/html:/var/www/html:' /etc/nginx/sites-available/default

#启动服务
RUN service nginx start
RUN service php5-fpm start

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
