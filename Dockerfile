FROM python:2.7

WORKDIR /crawler

COPY . /crawler

RUN \
    sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \    
    apt-get update -y && \
    apt-get install -y modemmanager && \
    apt-get upgrade -y && \
    apt-get install -y apt-transport-https apt-utils ca-certificates \
    software-properties-common curl git htop man unzip vim nano wget \ 
    net-tools iputils-ping python-pip && \    
    apt-get update    

RUN pip install requests &&\
    pip install bs4 &&\
    pip install lxml

CMD (python crawler-RdL.py && tail -f >> /dev/null)