FROM ubuntu:latest


RUN apt-get update -y;
RUN apt-get upgrade -y;
RUN apt-get install python3 python3-pip git -y

WORKDIR /opt
RUN git clone https://github.com/izm1chael/CTIReporter.git

WORKDIR /opt/CTIReporter
RUN mkdir content
RUN mkdir user
RUN pip3 install -r requirements.txt


EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]