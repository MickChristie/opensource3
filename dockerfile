FROM ubuntu:20.04

RUN apt update && apt -y upgrade
RUN apt install git python3 python3.pip

RUN pip3 install essential_generators

CMD ["python3","main.py"]
