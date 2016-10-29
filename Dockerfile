FROM ubuntu:trusty-20161006

RUN apt-get update

RUN apt-get install -y openssh-server

RUN mkdir /var/run/sshd

RUN echo 'root:password' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

ADD docker/sources.list ./
RUN mv sources.list /etc/apt/sources.list

RUN apt-get clean
RUN apt-get update

RUN apt-get install -y nginx
RUN apt-get install -y php5-fpm

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
