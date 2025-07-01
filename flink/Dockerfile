FROM flink:1.19

RUN apt-get update && apt-get install -y python3 python3-pip wget \
    && ln -s /usr/bin/python3 /usr/bin/python


COPY jars/*.jar /opt/flink/usrlib/
