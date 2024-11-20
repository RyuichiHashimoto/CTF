FROM nvidia/cuda:12.6.0-devel-ubuntu20.04
# FROM python:3.11



ARG WORKING_DIR="/home/work"
ARG project_name="poetryDev"
WORKDIR ${WORKING_DIR}

# timezone
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
#ENV POETRY_HOME=/opt/poetry


ENV SHELL=/bin/bash
RUN apt-get update -y && apt-get install vim net-tools sqlite3 build-essential graphviz default-jre fonts-ipafont hashcat software-properties-common curl vim net-tools sqlite3 git wget -y && apt-get clean


# Step1: Add deadsnakes PPA and install Python3.11
RUN add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get update -y && \
    apt-get install -y python3.11 python3.11-distutils python3.11-venv && \
    ln -sf /usr/bin/python3.11 /usr/bin/python3 && \
    ln -sf /usr/bin/python3.11 /usr/bin/python

#     
#RUN apt install python2 && \
    #curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o /tmp/get-pip.py && \
#    python2 /tmp/get-pip.py

# Step1: python3.9 install
# apt install software-properties-common -y && \
# add-apt-repository ppa:deadsnakes/ppa && \ 
# apt install python3.9 -y && \
# alias python=python3.9

# Step2: poetry config
#env PATH $PATH:$WORKING_DIR/.local/bin
ENV POETRY_HOME=/opt/poetry
ENV PATH $PATH:$WORKING_DIR/.local/bin
RUN apt install curl -y && \
mkdir /opt/poetry/bin -p && \
# apt install python3.9-distutils -y && \
curl -sSL https://install.python-poetry.org | python3.11 -  && \
cd /usr/local/bin && ln -s /opt/poetry/bin/poetry  && \
poetry config virtualenvs.in-project true
#poetry config virtualenvs.create true



#CMD
CMD ["bash"]
